'''
titile : 查询预审批过程
author:张来明
date:20190523
version:python3.7.3
'''

from data import *
from basic_method import *
import requests
import unittest
import json
import time

class ProProgress(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.url_list = ['10.139.60.88:8188','10.139.60.171:8088','10.138.61.93:8188','10.139.60.17:8188','10.139.60.61:8188']
        #输入要查询的GUID
        self.pre_check_guid = {"PreCheckGUID":"2804f871b2c647658089874031544c91"}
    def pro_progress(self):
        ''' 调用预审批过程查询接口'''
        for base_url in self.url_list:
            self.url = 'http://'+base_url+'/PreCheckService/GetPreScreenResultList'
            res = requests.post(self.url,json=self.pre_check_guid,headers=headers)
            dict_res = json.loads(res.text)
            if dict_res['Message'] == "查询成功！":
                print("查询地址为:",self.url)
                print("查询预审过程相应体为：",dict_res)
                break
        else:
            print("未查到数据")
    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    #构建测试集
    suite = unittest.TestSuite()
    #添加测试用例
    suite.addTest(ProProgress("pro_progress"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)