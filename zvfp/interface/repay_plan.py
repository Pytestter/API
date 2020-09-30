'''
titile : 还款计划查询接口
author:张来明
date:20190530
version:python3.7.3
'''
from data import  base_data
from basic_method import *

class RepayPlan:
    def __init__(self):
        #定义请求头
        self.headers = base_data.headers
        self.url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/repay-schedule'
        #定义查询的bid参数
        self.data = {"bid":"1040335"}
    def  test_repay_plan(self):
        response = ApiMethod(self.url,self.data,self.headers).post_request()

if __name__ == "__main__":
    repay_plan = RepayPlan()
    res = repay_plan.test_repay_plan()
