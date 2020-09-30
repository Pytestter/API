'''
直接调路由接口
'''
from select_route import *


if __name__ == '__main__':
    route = Route()
    token = route.route_init()  # 初始化
    apply_amount = '10000'
    applyPeriod = "6"
    supplementCustomerType = "VIP客户"
    customerMark = "4"
    serviceCode = "route"
    #直接调用路由接口
    route.route_select(serviceCode,token, apply_amount,applyPeriod,supplementCustomerType, customerMark)
    #直接调用路由查询接口
    route.route_query(token, route.id_no, route.product_code, route.name, fund_code=None)