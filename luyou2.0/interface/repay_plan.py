'''
titile : 还款计划查询接口
author:张来明
date:20200805
version:python3.7.3
'''
from data import base_data
import requests
import json
from basic_method import *
import time
class RepayPlan:
    def __init__(self):
        #定义请求头
        self.headers = base_data.headers
        self.url = 'http://api-gateway-t3.dev.vcredit.com.local/fund/repay-schedule'
        #定义查询的bid参数
        self.data = {"bid":"969458"}
    def  test_repay_plan(self):
        response = ApiMethod(self.url,self.data,self.headers).post_request()

if __name__ == "__main__":
    repay_plan = RepayPlan()
    res = repay_plan.test_repay_plan()
