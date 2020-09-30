'''
titile : 转担保
author:张来明
date:20190703
version:python3.6.5
'''

from data import *
from MongoClient import Mongo
from basic_method import *
import time

class Guarantee:
    def __init__(self):
        self.headers = headers
        self.url = guarantee_url

    def test_guarantee(self):
        '''
        转担保记录
        '''
        pass

    def test_guarantee_query(self):
        '''
        转担保结果查询{batchno}  
        '''
        pass


    def tearDown(self):
        pass

if __name__ == '__main__':
    guarantee = Guarantee()
    guarantee.test_guarantee()