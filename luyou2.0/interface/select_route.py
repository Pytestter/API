'''
预筛选->预筛选成功后路由->路由
'''
from data import base_data
from data import comm
from data import info_generator
from data.BankCardNumber import GetBankCardNumber
from basic_method import *
from faker import Faker
import product
import requests
import time
import os
import datetime


class Route:
    def __init__(self):
        self.i=1
        self.j=1
        self.headers = base_data.headers
        self.url = base_data.route_url
        self.faker = Faker('zh_CN')
        self.id_no = self.faker.ssn(min_age=22, max_age=49)
        self.name = self.faker.name()
        self.phone = info_generator.create_phone()
        self.product_code = product.product_code(default=False)
        # useRandom=True 随机产生一个银行卡号,useRandom=False可选择银行
        self.bank_info = GetBankCardNumber().getBankCardNumber(useRandom=True)

    def route_init(self):
        '''调用初始化接口,并返回token'''
        print("=" * 30 + "正在调用初始化接口" + "=" * 30)
        #调用产品编码方法获取产品编码,defualt=False可以选择产品,defualt=True则默认为豆豆产品
        init_data = comm.init_data(self.id_no, self.name, self.product_code)
        res = ApiMethod(self.url, init_data, self.headers).post_request()
        with open("../data/pre_approval.txt", "a+", encoding="utf-8") as file:
            file.write(time.strftime("%Y-%m-%d %H:%M:%S") + ":" + res['data']['routeAuthToken'] + "\n")
        data_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        self.path = '../data/request_data/' + data_time + '-' + res['data']['routeAuthToken'] + '/'
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        write_to_file(self.path, "1初始化请求报文", init_data)
        write_to_file(self.path, "2初始化响应报文", res)
        print("=" * 30 + "初始化接口调用完毕" + "=" * 30)
        return res['data']['routeAuthToken']

    def route_select(self, serviceCode,token,apply_amount,applyPeriod,supplementCustomerType, customerMark):
        '''调用预筛选-路由接口'''
        print("=" * 30 + "正在调用路由或者预筛选接口" + "=" * 30)
        select_data = comm.select_data(serviceCode,token, self.name, self.id_no, self.product_code, self.phone, apply_amount,
                                       self.bank_info, supplementCustomerType, customerMark, applyPeriod, sync=False)
        res = ApiMethod(self.url, select_data, self.headers).post_request()
        write_to_file(self.path, "3预筛选请求报文", select_data)
        write_to_file(self.path, "4预筛选响应报文", res)
        print("=" * 30 + "预筛选接口调用完毕" + "=" * 27)

    def route_select_query(self, token):
        '''调用预筛选查询接口'''
        print("=" * 30 + "正在调用预筛选查询接口" + "=" * 24)
        time.sleep(3)
        print("预筛选第{}次查询:".format(self.i))
        select_query_data = comm.select_query_data(token)
        res = ApiMethod(self.url, select_query_data, self.headers).post_request()
        self.i = self.i + 1
        if res['data']['status'] == 'screening' and self.i <= 10  :
            return self.route_select_query(token)

        print(("=" * 30 + "预筛选查询接口调用完毕" + "=" * 24))
        write_to_file(self.path, "5预筛选查询请求报文", select_query_data)
        write_to_file(self.path, "6预筛选查询响应报文", res)
        return res['data']['status']

    def route_success(self, token, product_code):
        '''预筛选成功后路由'''
        print("=" * 30 + "正在调用预筛选成功后路由接口" + "=" * 19)
        self.route_success_data = comm.route_success_data(token,product_code)
        self.fund_code = self.route_success_data['fundCode']
        print(self.fund_code)
        res = ApiMethod(self.url, self.route_success_data, self.headers).post_request()
        write_to_file(self.path, "7预筛选成功后路由请求报文", self.route_success_data)
        write_to_file(self.path, "8预筛选成功后路由响应报文", res)

        print("=" * 30 + "预筛选成功后路由接口调用完毕" + "=" * 24)


    def route_query(self,token, id_no,product_code,name,fund_code=None):
        '''路由查询'''
        print("=" * 30 + "正在调用路由查询接口" + "=" * 24)
        print("资方路由第{}次查询:".format(self.j))
        route_query_data = comm.route_query_data(token,id_no,product_code,name,fund_code)
        res = ApiMethod(self.url, route_query_data, self.headers).post_request()
        time.sleep(2)
        self.j = self.j + 1
        if (res['data']['status'] == 'routing' and self.j <= 10) or (res['data']['status'] == 'timeout' and self.j <= 10 ):
            return self.route_query(token, self.id_no, self.product_code, self.name)
        else:
            write_to_file(self.path, '9路由查询请求报文', route_query_data)
            write_to_file(self.path, '10路由查询响应报文', res)
        print("=" * 30 + "路由查询接口调用完毕" + "=" * 24)


if __name__ == '__main__':
    '''主流程'''
    while True:
        route = Route()
        token = route.route_init()  # 初始化
        apply_amount = '10000'
        applyPeriod = "6"
        supplementCustomerType = "1"
        customerMark = "正常客户"
        serviceCode = "prescreen"
        route.route_select(serviceCode,token, apply_amount,applyPeriod,supplementCustomerType, customerMark)  # 预筛选
        time.sleep(2)
        status = route.route_select_query(token)  # 预筛选查询
        if status == 'screenPassed':
            route.route_success(token, route.product_code)  # 预筛选成功后路由
            route.route_query(token,route.id_no,route.product_code, route.name,route.fund_code)
        else:
            print("预筛选出现异常,请仔细核查预筛选是否正常!")

