'''
titile : 存放基础数据
author:张来明
date:20200604
version:python3.6.5
'''
import time
#from read_excel import bank_code
data = str(int(time.time()))
import re
#请求头信息
headers = {
    "Content-Type":"application/json",
    "apiToken":"e6475549-4681-4b12-9ca0-d28c0e03230a",
    "sync":"false",
    "X-CLIENT-ID":"123"
        }



#所有的url地址：
route_url = 'http://api-gateway-t3.dev.vcredit.com.local/route/command'   #路由
loan_url = 'http://api-gateway-t3.dev.vcredit.com.local/payment/loan'     #放款
sign_url = 'http://api-gateway-t3.dev.vcredit.com.local/fund/entrustApply'    #签约申请
sign_verify_url = 'http://api-gateway-t3.dev.vcredit.com.local/fund/entrustVerify'    #签约确认
sign_query_url ='http://api-gateway-t3.dev.vcredit.com.local/fund/entrustQuery'    #签约查询








