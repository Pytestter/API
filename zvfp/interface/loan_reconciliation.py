'''
titile : 放款对账接口
author:张来明
date:20191111
version:python3.7.3
'''
from data import *
from comm import *
import requests
import unittest
class LoanReconciliation(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #定义请求头
        self.headers = headers
        self.url = loan_reconcialation_uat_url
        self.data  = loan_reconciliation_data("zyxj","20240509")
        print("请求参数为{}".format(self.data))
    def test_loan_reconciliation(self):
        print("请求地址：",self.url)
        response = requests.post(self.url,json=self.data,headers=self.headers)
        print("响应报文为：{}".format(response.text))


if __name__ == "__main__":
    #构建测试集
    suite = unittest.TestSuite()
    suite.addTest(LoanReconciliation("test_loan_reconciliation"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)