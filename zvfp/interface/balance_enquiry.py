'''
titile : 华润余额查询接口
author:张来明
date:20190507
version:python3.7.3
'''
from data import *
from data import huarun
import json
import requests
import unittest
class Balance(unittest.TestCase):
    def setUp(self):
        #定义请求头
        self.headers = headers
        self.url = yue_query_url_url
    def test_balance_enquiry(self):
        #传入余额查询请求数据
        data  =  Data1.balance_enquiry_data
        #将数据转化为json格式
        json_data = json.dumps(data)
        #使用requests库请求地址，并传入data和headers参数
        res = requests.post(self.url,headers=self.headers,data=json_data)
        print("余额查询结果为：",res.text)
    def tearDown(self):
        pass
if __name__=='__main__':
    #构建测试集
    suite = unittest.TestSuite()
    suite.addTest(Balance("test_balance_enquiry"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)