'''
titile : 代扣（正常还款）
author:张来明
date:20190704
version:python3.6.5
'''
import base_data
from comm import *
import requests
import unittest
import json
from MongoClient import Mongo
import time

class Deduct(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.url = deduct_url
        #batch_no和transactionId
        self.query_url = deduct_query_url+'batchNo=33512'+'&transactionId=20200825601179569'
        self.deduct_data = deduct_data()
        print("代扣请求入参：",self.deduct_data)

    def test_deduct(self):
        '''
        代扣接口
        '''
        response = requests.post(self.url,json=self.deduct_data,headers=self.headers)
        #输出代扣返回结果
        print ("代扣请求状态码：",response.status_code)
        print ("代扣返回结果为：",response.text)
    def test_query_repay_result(self):
        '''
        代扣结果查询接口
        '''
        print("查询地址为:",self.query_url)
        res = requests.get(self.query_url,headers=self.headers)
        #输出扣款结果
        print("代扣查询请求状态码:{}".format(res.status_code))
        print("代扣查询结果为为:{}".format(res.text))

    def test_mongo_daikou(self):
        '''查询扣款结果'''
        pass
    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    #构建测试集
    suite = unittest.TestSuite()
    suite.addTest(Deduct("test_deduct"))
    #suite.addTest(Deduct("test_query_repay_result"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)