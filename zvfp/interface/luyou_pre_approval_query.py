# -*- coding: utf-8 -*-
'''
titile : 路由初始化+查询接口
author:张来明
date:20190522
version:python3.7.3
'''
from data import base_data
from data import luyou
import os
import product
import datetime
from basic_method import *
import requests
from faker import Faker
from api_values_check_cls import ApiFieldValuesCheck

class Init_Query:
    def __init__(self):
        self.headers = base_data.headers
        self.url = base_data.luyou_init_url
        faker = Faker('zh_CN')
        self.id_number = faker.ssn(min_age=22, max_age=49)
        self.name = faker.name()
        #产品选择，default=True 默认为豆豆
        self.product_code = product.product_code(default=False)
        self.excel_path = './data/api_values_check.xlsx'
        self.risk_sheet_name = '初始化'
        self.api_check = ApiFieldValuesCheck(self.excel_path,self.risk_sheet_name)
        self.i = 1
    def test_ly_init_query(self,routeAuthToken):
        '''调用初始化接口'''
        if routeAuthToken == None:
            print("=" * 30 + "正在调用初始化接口" + "=" * 30)
            self.data = luyou.init_data(self.id_number, self.name, self.product_code, routeAuthToken)
            print("资方路由初始化请求报文{}:".format(json.dumps(self.data,indent=4,ensure_ascii=False)))
            # 调用初始化接口
            results = requests.post(self.url, json=self.data, headers=self.headers)
            res = results.json()
            self.api_check.api_field_test(res)
            data_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
            self.path = './data/request_data/' + data_time + '-' + res['data']['routeAuthToken'] + '/'
            if not os.path.exists(self.path):
                os.mkdir(self.path)
            print("资方路由初始化产生的token为:", json.dumps(res['data']['routeAuthToken'], indent=4, ensure_ascii=False))
            write_to_file(self.path, '1初始化请求报文', self.data)
            write_to_file(self.path, '2初始化响应报文', res)
            print("=" * 30 + "初始化接口调用完毕" + "=" * 30)
            return (res['data']['routeAuthToken'], self.data['customerName'], self.data['idCardNo'], self.data['productCode'],
            self.path)
        else:
            if self.i == 1:
                print("=" * 30 + "正在调用预审批查询接口" + "=" * 30)
            print("第{}次调用授信查询接口".format(self.i))
            self.data = luyou.init_data(self.id_number, self.name, self.product_code, routeAuthToken)
            results = requests.post(self.url, json=self.data, headers=self.headers)
            res = results.json()
            if res['data']['status'] !='passed' and res['data']['status'] !='failed' and self.i<20 :
                self.i+=1
                time.sleep(10)
                return self.test_ly_init_query(routeAuthToken)
            else:
                print("预筛选查询请求报文{}".format(json.dumps(self.data,indent=4,ensure_ascii=False)))
                print("预筛选查询响应报文{}".format(json.dumps(res,indent=4,ensure_ascii=False)))
                write_to_file(self.path, '5预审批查询请求报文', self.data)
                write_to_file(self.path, '6预审批查询响应报文', res)
                print("=" * 30 + "预审批查询接口调用完毕" + "=" * 30)
                return res






if __name__ == '__main__':
    #64e3682275a9421c8817682cf19a4c21
    routeAuthToken = None
    init = Init_Query()
    init.test_ly_init_query(routeAuthToken)
