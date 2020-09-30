'''
titile : 文件上传接口（固定数据）
author:张来明
date:20200427
version:python3.7.3
'''
import basic_method
import time
import requests
from MongoClient import Mongo
import wenjianpost_data
from data import *


class FilePost(unittest.TestCase):
    def setUp(self):
        # 传入头部信息
        self.headers = headers
        self.url = document_upload_url
        self.data = wenjianpost_data.upload_data()

    def test_file_post(self):
        '''
        文件上传接口   
        '''
        response = basic_method.ApiMethod(self.url, self.data, self.headers).post_request()


    def test_filepost_query(self):
        '''
        文件上传结果查询{batchNo}
        '''
        query_url = self.url + self.res['data']['batchNo']
        self.i += 1
        print("第{}查询文件上传结果".format(self.i))
        time.sleep(1)
        res = requests.get(url=query_url, headers=self.headers)
        if res.json()['data'][0]['status'] == 'pending' and self.i <= 10:
            return self.document_result_qurey()
        else:
            print(res.json())


if __name__ == '__main__':
    # 构建测试集
    suite = unittest.TestSuite()
    suite.addTest(Filepost("test_file_post"))
    suite.addTest(Filepost("test_mongo_filepost"))
    # suite.addTest(Filepost("test_filepost_query"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
