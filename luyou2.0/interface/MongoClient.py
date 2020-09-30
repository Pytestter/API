'''
titile : 连接MongoDB数据库，并查询对应库下面的数据
author:张来明
date:20190422
version:python3.7.3
'''
import pymongo
class Mongo:
    #创建MongoDB的连接对象，连接数据库
    def __init__(self,db):
        self.client =  pymongo.MongoClient(host='10.138.61.95',port=27017)
        self.db = self.client[db]
    def query_pre_approval_result(self,thread_id):
        '''查询预审批结果'''
        #指定数据库
        #指定集合，查询初始化内容
        collections = self.db.pre_approval_instruction
        #查询结果
        results=collections.find_one({'thread_id':thread_id})
        return results
    def query_file_post_result(self,transaction_id):
        '''查询文件是否上传成功'''
        #指定数据库
        db = self.client.fund_uat
        #指定集合，查询初始化内容
        collections = db.document_upload_instruction
        self.transaction_id = transaction_id
        #查询结果
        results=collections.find_one({'transaction_id':self.transaction_id})
        #输出文件上传查询结果
        print("查询文件上传结果为(数据库)：",results)
       # print("查询文件上传结果为："+"status:"+results['status']+"      ","message："+results['message'])
    def query_loan_result(self,bid):
        '''查询放款是否成功'''
        #指定数据库
        db = self.db
        #指定集合，查询初始化内容
        collections = db.loan_instruction
        self.bid = bid
        #查询结果
        results=collections.find_one({'bid':self.bid})
        return results
    def query_kh_result(self,transaction_id):
        '''查询是否开户成功'''
        #执行数据库
        db = self.client.fund_uat
        #指定集合
        collections = db.account_open
        self.transaction_id = transaction_id
        #查询结果：
        results = collections.find_one({'transaction_id':self.transaction_id})
        #查询开户结果
        print("开户结果为："+"status:"+results['status']+"         ","message:"+results['message'])

    def query_dk_result(self,batch_no):
        '''查询代扣是否成功'''
        #执行数据库
        db = self.client.fund_uat
        #指定集合
        collections = db.deduct_instruction
        self.batch_no = batch_no
        #查询结果：
        results = collections.find_one({'batch_no':self.batch_no})
        #查看代扣结果
        print("代扣结果为："+"status:"+results['status']+"         ","message:"+results['message'])
    def query_fund_result(self,id):
        '''查询资方请求结果'''
        #指定数据库
        #指定集合，查询初始化内容
        print("=" * 40 + "以下为请求资方的入参和出参" + "=" * 40)
        collections = self.db.funding_request_record
        #查询结果
        results=collections.find({'instruction_id':id})
        for result in results:
            if result:
                if result['request_body']:
                    print('request_body:{}'.format(result['request_body']),end='\n')
                    print('response_body:{}'.format(result['response_body']))
            else:
                print("没有查到与资方相关的请求响应数据！！")
    def query_sign_result(self,apply_no):
        '''查询签约申请'''
        # 指定集合，查询初始化内容
        collections = self.db.entrust_apply_information
        # 查询结果
        results = collections.find_one({'apply_no':apply_no})
        return results

    def query_bank_result(self, register_id):
        '''绑卡数据'''
        # 指定集合，查询初始化内容
        collections = self.db.pre_apply_instruction
        # 查询结果
        results = collections.find_one({'register_id': register_id})
        return results

if __name__ == '__main__':
   result = Mongo('fund_uat').query_bank_result('1296725852784173058')
   print(result)

