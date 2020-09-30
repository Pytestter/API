'''
titile : 文件下载接口
author:张来明
date:20190510
version:python3.6.5
'''
from comm import *
import basic_method
import base_data
import requests
import unittest
import json


class FileObtain:
    def setUp(self):
        self.headers = base_data.headers
        self.url =  base_data.ducument_obtain_url
        #batch_no
        self.query_url = base_data.ducument_obtain_query_url + "69b72cb1-377f-46da-b9b7-24ceff5f4202" + "?transactionId=zlmfilobtain15922750701"
        fund_code = 'FDCD000011'
        thread_id = 'XzgjLS1ZWiVTMk44'
        self.data = documet_obtain_data(fund_code,thread_id)
        #print("请求入参为：{}".format(self.data))
    def test_file_obtain(self):
        '''
        调用文件下载接口
        '''
        response = basic_method.ApiMethod(self.url,self.data,self.headers).post_request()

    def test_file_obtain_query(self):
        '''
        调用文件下载查询接口{batchNo}
        '''
        res  = requests.get(self.query_url,headers=self.headers)
        #将查询返回内容转化为字典
        print("响应报文:",res)
        #dict_data = json.loads(res.text)
        #print("查询文件下载结果为："+"status:"+dict_data['data'][0]['status']+"    "+"message:"+dict_data['data'][0]['message'])

    def tearDown(self):
        pass

if __name__ == '__main__':
    #构建测试集
    suite = unittest.TestSuite()
    #测试文件下载接口
    suite.addTest(FileObtain("test_file_obtain"))
    #调用文件下载查询接口
    #suite.addTest(FileObtain("test_file_obtain_query"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)