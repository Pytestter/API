'''
titile : 执行指定目录下的对应测试文件，并发送测试报告
author:张来明
date:20190429
version:python3.7.3
'''
import time, sys
sys.path.append('./test')
#sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from selenium import webdriver
#from db_fixture import test_data


# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './test'
testsuit = defaultTestLoader.discover(test_dir, pattern='*.py')


if __name__ == "__main__":
    #test_data.init_data() # 初始化接口测试数据
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告输出',description='运行环境：Requests, unittest ')
    runner.run(testsuit)
    fp.close()
    #自动打开测试报告
    # browser = webdriver.Chrome()
    # browser.get('file:///D:/zlm/code/fund/'+filename)

