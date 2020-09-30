'''
titile : 资方路由预审批接口
author:张来明
date:20190522
version:python3.7.3
'''
from data import luyou
from MysqlClient import Mysql
from MongoClient import Mongo
from luyou_pre_approval_query import  Init_Query
from data import base_data
from data import  info_generator
from basic_method import *
import time
import BankCardNumber
from api_values_check_cls import ApiFieldValuesCheck

thread_Ids = ''
class PreApproval:
    def __init__(self,pre_list):
        self.headers = base_data.headers
        self.url = base_data.luyou_pre_url
        #产生一个手机号
        phone = info_generator.create_phone()
        #useRandom=True 随机产生一个银行卡号,useRandom=False可选择银行
        bank_info = BankCardNumber.GetBankCardNumber().getBankCardNumber(useRandom=True)
        print("银行卡信息为:",bank_info)
        self.data = luyou.pre_apro_data(pre_list, phone, bank_info)
        #将本次请求的token值保存到txt
        with open ("data/pre_approval.txt", "a+", encoding="utf-8") as file:
            file.write(time.strftime("%Y-%m-%d %H:%M:%S")+":"+pre_list[0]+"\n")
        self.path = pre_list[4]

    def test_pre_approval(self):
        '''
        调用资方路由预审批接口
        '''
        print("=" * 30 + "正在调用预审批接口" + "=" *30)
        res = ApiMethod(self.url,self.data,self.headers).post_request()
        print("=" * 30 + "预审批接口调用完毕" + "=" * 30)
        write_to_file(self.path,"3预审批请求参数",self.data)
        write_to_file(self.path,"4预审批响应参数",res)
        return  res
    def test_pre_approval_result(self):
        '''
        查询预审批结果()
        '''
        print("=" * 30 + "下面为授信对应的资方信息" + "=" * 30)
        db = 'fund_uat' if '2' in self.url else 'fund_sit2'
        mysql =Mysql(db)
        mongo = Mongo(db)
        time.sleep(2)
        thread_Ids = mysql.query_route_pre_approval_result(self.data['routeAuthToken'])
        if thread_Ids != None :
            for thread_id in thread_Ids:
                if thread_id != 'None':
                    results = mongo.query_pre_approval_result(thread_id)
                    channel_code = mysql.query_channel_code(results['fund_code'])
                    loan_data = [self.path,db,results['thread_id'],channel_code]
                    return loan_data
                else:
                    print("授信未通过")
                    # results_id =results['_id']
                    # mongo.query_fund_result(str(results_id))
        #         else:
        #             print("没有请求预审批接口！")
        # else:
        #     print("未调用资方授信接口！")


if __name__ == '__main__':
    while True:
        print("="*30+"预审批调用链"+"="*30)
        #初始化接口实例化
        init_query = Init_Query()
        #调用初始化接口
        res_init = init_query.test_ly_init_query(routeAuthToken=None)
        #申请金额，申请期数，客户类型，客户标识
        pre_list = res_init + ('12000', '6', "66客户", "6")
        #授信接口
        pre_approval = PreApproval(pre_list)
        res = pre_approval.test_pre_approval()
        risk_sheet_name = '预审批'
        api_check = ApiFieldValuesCheck(init_query.excel_path,risk_sheet_name)
        api_check.api_field_test(res)
        #授信查询接口
        if res['message'] == '成功':
            res = init_query.test_ly_init_query(res_init[0])
            risk_sheet_name = '预审批查询'
            api_check = ApiFieldValuesCheck(init_query.excel_path, risk_sheet_name)
            api_check.api_field_test(res)
            pre_approval.test_pre_approval_result()


