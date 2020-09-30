'''
titile : 还款推送接口(代偿)
author:张来明
date:20190703
version:python3.6.5
'''
from data import base_data
from data import comm
import requests
import unittest
import json
from MongoClient import Mongo
import time

class Repay(unittest.TestCase):
    def setUp(self):
        self.headers = base_data.headers
        self.url = base_data.repay_info_url
        #fund_code 和 batch_no
        self.query_url = base_data.repay_info_url + '/FDCD100002&fdjkafdal34247'
        self.dada = comm.repay_info_data()
        print("请求参数为：",self.dada)

    def test_repay_batch(self):
        '''
        还款推送接口
        '''
        response = requests.post(self.url,json=self.dada,headers=self.headers)
        #输出放款返回结果
        print ("还款推送状态码：",response.status_code)
        print ("还款推送返回结果为：",response.text)

    def test_query_repay_result(self):
        '''
        还款推送查询接口
        '''
        print("还款推送查询地址：",self.query_url)
        res = requests.get(self.query_url,headers=self.headers)
        #输出放款查询结果
        print("还款推送查询请求状态：",res.status_code)
        print("还款推送查询结果为",res.text)

    def tearDown(self):
        pass

if __name__ == '__main__':
    #构建测试集
    suite = unittest.TestSuite()
    #还款推送
    suite.addTest(Repay("test_repay_batch"))
    #还款推送结果查询
    #suite.addTest(Repay("test_query_repay_result"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)