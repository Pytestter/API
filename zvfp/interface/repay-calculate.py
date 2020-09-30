'''
titile : 还款试算接口
author:张来明
date:20191127
version:python3.6.5
'''
from base_data import *
from comm import *
import unittest
import requests
class Calculate(unittest.TestCase):
    def setUp(self):
        #定义请求头
        self.headers = headers
        self.url = calculate_url
        self.apply_period = '1'   #期数
        self.bid = '21350512'    #bid
        self.planAmount = '18000'
        self.productCode= 'PDCD000032'
        self.data = repay_calculate_data(self.apply_period,self.bid,self.planAmount,self.productCode)
        print("请求入参为{}".format(self.data))
    def test_calculate(self):
        res = requests.post(self.url,json=self.data,headers=self.headers)
        print("请求状态码为：",res.status_code)
        print("响应报文为：",res.text)
    def test_mongo_calculate(self):
        '''试算查询结果'''
        pass
    def tearDown(self):
        print("试算结束")


if __name__ == "__main__":
    # 构建测试集
    suite = unittest.TestSuite()
    #添加测试用例
    suite.addTest(Calculate("test_calculate"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

