'''
titile : 资金规模查询
author:张来明
date:20190510
version:python3.7.3
'''
import base_data
import requests
import  json
import basic_method

def fund_info_query():
    url = base_data.fund_info_url
    res = requests.get(url).text
    print(res)


if __name__ == '__main__':
    fund_info_query()
