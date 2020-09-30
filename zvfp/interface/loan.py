'''
titile : 进件申请接口（请款）
author:张来明
date:20190425
version:python3.7.3
'''
import base_data
from data import comm
import unittest
import basic_method
import requests
from MongoClient import Mongo
import time


class Loan:
    def __init__(self,loan_list):
        self.headers = base_data.headers
        self.url = base_data.loan_url
        self.query_url = base_data.loan_query_url
        self.data = comm.loan_data(loan_list) #从数据库查询
        self.i = 1
        self.loan_list = loan_list
        with open ("data/loan.txt", "a+", encoding="utf-8") as file:
            file.write(time.strftime("%Y-%m-%d %H:%M:%S")+":"+self.data['instructions'][0]['bid']+"\n")
        basic_method.write_to_file(loan_list[0],"放款请求报文", self.data)
    def test_loan(self):
        '''放款接口'''
        print("放款的bid为",self.data['instructions'][0]['bid'])
        res = requests.post(url=self.url,json=self.data,headers=self.headers)
        print("放款响应报文为:",res.text)
    def test_query_fk_result(self):
        '''查询放款结果接口  +response.text'''
        print("放款查询地址",self.query_url)
        res = requests.get(self.query_url,headers=self.headers)
        #输出放款查询结果
        print(res.status_code)
        print("放款查询结果为：",res.text)

    def test_mongo_loan(self):
        '''通过数据库查询放款结果'''
        mongo = Mongo('payment_sit2')
        bid = self.data['instructions'][0]['bid']
        time.sleep(2)
        results = mongo.query_loan_result(bid)
        print("第{}次查询放款".format(self.i))
        if results['status'] == 'PENDING' and self.i<=10:
            self.i += 1
            return self.test_mongo_loan()
        elif results['status'] == 'FAIL':
            return self.test_loan(self,self.loan_list)
        else:
            print("放款结果为：",results)


if __name__ == '__main__':
    loan_list = ['../data/loan_data/','fund_uat','LS0tOSUlJVY0OF9K','ylbank']
    loan = Loan(loan_list)
    loan.test_loan()
    loan.test_mongo_loan()
