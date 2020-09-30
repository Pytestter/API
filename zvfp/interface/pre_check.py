# -*- coding: utf-8 -*-
'''
titile : 撞库
author:张来明
date:20200817
version:python3.7.3
'''
import base_data
import comm
import basic_method
import info_generator
import os
import product
import time
import datetime
from basic_method import *
import requests
from faker import Faker
from data import *

class PreCheck:
    def __init__(self):
        self.headers = base_data.headers
        self.url = base_data.pre_check_url
        self.agreement_url = base_data.query_agreement_url
        faker = Faker('zh_CN')
        self.id_number = faker.ssn(min_age=22, max_age=49)
        self.name = faker.name()
        self.phone = info_generator.create_phone()

    def test_pre_check(self):
        '''调用撞库接口'''
        self.data = comm.test_pre_check(self.phone, self.id_number, self.name)
        print("撞库请求参数:",self.data)
        write_to_file("data/zhongyuan/", '撞库请求参数', self.data)
        res = ApiMethod(self.url,self.data,self.headers).post_request()
        write_to_file("data/zhongyuan/", '撞库请求参数', res)
    def test_agreement_query(self):
        "协议地址查询"
        self.bank_card_no = GetBankCardNumber().getBankCardNumber(useRandom=True)[1]
        self.agreement_data = comm.agreement_query(self.id_number, self.name, self.bank_card_no, self.phone)
        #self.agreement_data = comm.agreement_query1()
        print(self.agreement_data)
        write_to_file("data/zhongyuan/", '协议查询请求参数', self.agreement_data)
        res_url = ApiMethod(self.agreement_url,self.agreement_data,self.headers).post_request()

if __name__ == '__main__':
    pre_check = PreCheck()
    pre_check.test_pre_check()
    pre_check.test_agreement_query()
