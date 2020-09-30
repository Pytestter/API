'''
titile : 测试【测试报告】输出
author:张来明
date:20190430
version:python3.7.3
'''
import unittest
import requests
# import sys



# def add(a,b):
#     return a+b
class Taobao(unittest.TestCase):
    def setUp(self):
        pass
    def test_taobao(self):
        url = 'http://www.taobao.com'
        res = requests.get(url)
        #print(res.status_code)
        self.assertEqual(res.status_code, 200)
    def tearDown(self):
        pass
# if __name__ == '__main__':
#     unittest.main()
