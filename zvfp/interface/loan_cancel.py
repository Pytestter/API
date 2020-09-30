'''
titile : 放款取消
author:张来明
date:20191112
version:python3.7.3
'''
from data import *
import comm
from basic_method import *
import time


class LoanCancel:
    def __init__(self,thread_id):
        self.headers = headers
        self.url = loan_cancel_url
        self.query_url = loan_query_cancel_url
        self.data = comm.loan_cancel_data(thread_id)

    def loan_cancel(self):
        '''
        调用放款取消接口，只有放款失败的订单才能取消
        '''
        res = ApiMethod(self.url,self.data,self.headers).post_request()
        print("transactionId为：",self.data['transactionId'])

    def loan_cancel_query(self):
        '''
        调用查询放款取消结果
        '''
        self.query_url = loan_query_cancel_url+self.data['transactionId']
        res = requests.get(self.query_url,headers=self.headers)
        if res.json()['data']['status'] == 'pending':
            return loan_cancel_query()
        else:
            print("放款取消查询结果为:",res.json())

if __name__=='__main__':
    thread_id  = 'Rl8jMyNEJS1SIyMjLUslNzAjMzE='
    loan_cancel = LoanCancel(thread_id)
    loan_cancel.loan_cancel()
    loan_cancel.loan_cancel_query()
