'''
titile : 重放接口
author:张来明
date:20190710
version:python3.6.5
'''

import sys
sys.path.append("../data/luyou")
sys.path.append("../data/base")
import Data
import Data2
import Base
import requests
import unittest
import json
import time
from luyou_query import  Init_Query

class Pre_reset(unittest.TestCase):
    def setUp(self):
        self.headers = Base.headers
    def test_yushenpi_chongfang(self):
        '''
        调用预审批重放接口
        '''
        cf_url = 'http://api-gateway-t2.dev.vcredit.com.local/fund/continuePreApprovalNotify'
        data = Data2.chongfang_data
        #将字典转化为json字符串格式
        json_data = json.dumps(data)
        res = requests.post(cf_url,headers=self.headers,data=json_data)
        #预审批重放返回状态码
        print("预审批返回状态码为：",res.status_code)
        print("预审批结果为：",res.text)
    def tearDown(self):
        pass

if __name__ == '__main__':
    #构建测试集
    suite = unittest.TestSuite()
    #测试初始化接口
    suite.addTest(Pre_reset("test_yushenpi_chongfang"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)