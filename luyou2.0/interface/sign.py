'''
titile : 签约接口
author:张来明
date:20200804
version:python3.7.3
'''
'''
titile : 签约查询接口
author:张来明
date:20190530
version:python3.7.3
'''
import sys
import requests
import json
from data.base_data import *
from data.comm import *
from basic_method import *
import datetime
import os
from MongoClient import *

class Sign:
    def __init__(self, thread_id):
        # 定义请求头
        self.headers = headers
        self.url = sign_url  # 签约申请
        self.verify_url = sign_verify_url #签约确认
        self.query_url = sign_query_url #签约查询
        self.thread_id = thread_id
        self.sign_data = sign_data(thread_id)  #签约申请参数
        data_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        self.path = '../data/request_data/' + data_time + '-' + 'sign'+'-'+self.sign_data['applyNo'] + '/'
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def test_sign_apply(self):
        # 签约接口
        print("签约请求报文:",self.sign_data)
        res = ApiMethod(self.url, self.sign_data, self.headers).post_request()
        write_to_file(self.path,"1签约请求报文",self.sign_data)
        write_to_file(self.path,"2签约响应报文",res)
        return self.sign_data

    def test_sign_verify(self,apply_Id):
        # 签约确认接口
        self.verify_data = sign_verify_data(apply_Id)
        print("签约确认请求报文:",self.verify_data)
        res = ApiMethod(self.verify_url,self.verify_data, self.headers).post_request()
        write_to_file(self.path, "3签约申请确认请求报文", self.verify_data)
        write_to_file(self.path, "4签约申请确认响应报文", res)

    def test_sign_query(self,data):
        #签约查询接口
        self.query_data = sign_query(data)
        res = ApiMethod(self.query_url,self.query_data,self.headers).post_request()
        write_to_file(self.path, "5签约查询", self.query_data)
        write_to_file(self.path, "6签约申请确认响应报文", res)



if __name__ == "__main__":
    thread_id = 'WCNfUTNfWiVfTzg0SUxBUUdaJU8='
    sign = Sign(thread_id)
    #签约申请
    apply_data = sign.test_sign_apply()
    time.sleep(2)
    #查询签约状态
    apply_sign_status = Mongo('fund_sit2').query_sign_result(apply_data['applyNo'])
    if apply_sign_status == 'SUBMITTED':
        #签约确认
        sign.test_sign_verify(apply_data['applyNo'])
        sign.test_sign_query(data)
