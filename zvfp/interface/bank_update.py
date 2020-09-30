'''
titile :改卡接口
author:张来明
date:20190522
version:python3.7.3
'''

from data import *
from info_generator import *
from comm import *
import requests
import unittest
import json
import time


class BankUpdate(unittest.TestCase):
    def setUp(self):
        self.headers = headers
        self.url = bank_update_url
        #transactionId
        self.thread_id = 'X0kyUVI0TiVDVE5W'
        self.bid = '1063994'
        self.new_ac_name = create_name()
        self.data = bank_update_data(self.thread_id,self.bid)
    def test_bank_update(self):
        '''
        调用改卡接口
        '''
        res = requests.post(self.url,headers=self.headers,json=self.data)
        print("换卡对应的transactionid为",self.data['transactionId'])
        #预审批返回状态码
        print("换卡返回状态码为：",res.status_code)
        print("换卡结果为：",res.text)
    def test_query_bank_update(self):
        '''
        查询银行卡结果
        '''
        self.query_url = bank_query_update_url+'/'+self.data['transactionId']
        res = requests.get(self.query_url,headers=self.headers)
        print("查询银行卡改卡结果为:",res.text)
    def tearDown(self):
        pass

if __name__ == '__main__':
    #构建测试集
    suite = unittest.TestSuite()
    #测试初始化接口
    suite.addTest(BankUpdate("test_bank_update"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)