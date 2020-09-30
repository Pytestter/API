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
class Baidu(unittest.TestCase):
    def setUp(self):
        pass
    def test_baidu(self):
        url = 'http://www.baidu.com'
        res = requests.get(url)
        #print(res.status_code)
        self.assertEqual(res.status_code, 201)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()

# s = add(1,2)
# print(s)