'''
titile : 签约查询接口
author:张来明
date:20190530
version:python3.7.3
'''
import sys
import requests
import json
from data import *
from comm import *


class Sign:
    def __init__(self, thread_id):
        # 定义请求头
        self.headers = vbs_headers
        self.url = vbs_sign_url  # 签约申请
        self.verify_url = vbs_sign_verigy_url
        self.thread_id = thread_id
        self.data = vbs_sign_data(thread_id)
        data_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        self.path = '../data/request_data/' + data_time + '-' + 'sign'+'-'+self.data['applyId'] + '/'
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def test_sign_apply(self):
        # 签约接口
        res = ApiMethod(self.url, self.data, self.headers).post_request()
        write_to_file(self.path,"1签约请求报文",self.data)
        return self.data['applyId']

    def test_sign_verify(self, apply_Id):
        # 签约确认接口
        self.data = test_sign_verify(apply_Id)
        ApiMethod(self.verify_url, data, self.thread_id).post_request()

    def test_sign_query(self):
        #签约查询接口
        pass


if __name__ == "__main__":
    sign = Sign('VVVWXyM1XzlJNThKQyNfNjItQSU=')
    apply_Id = sign.test_sign_apply()
    sign.test_sign_verify(apply_Id)
