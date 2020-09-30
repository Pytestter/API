'''
titile : 连接Mysql数据库，并查询对应库下面的数据
author:张来明
date:20190817
version:python3.7.3
'''
import pymysql
from data import read_excel
import json
class Mysql:
    def __init__(self,db):
        #创建连接
        self.i = 1
        self.db = pymysql.connect(host='10.138.60.216', port=3306, user='root', passwd='Vcredit@67890', db=db,charset="utf8" )
        #创建游标
        self.cursor = self.db.cursor()
    def query_route_pre_approval_result(self,token):
        '''
        查询资方路由请求结果
        '''
        self.token = token
        #执行sql语句
        self.cursor.execute('SELECT fund_code,audit_status,thread_id FROM t_route_details where route_auth_token = %s',self.token)
        #获取第所有数据
        results = self.cursor.fetchall()
        print(results[0][0])
        if results:
            for data in results:
                print("资方路由的结果为：{}".format(data))
                fund_dict = json.load(open( "./data/fundcode.json", encoding="utf-8"))
                fund_name = fund_dict[results[0][0]]
                print("资方编码对应的资方为：{}".format(fund_name))
                yield data[2]
        #关闭数据库
        self.db.close()
    def query_channel_code(self,fund_code):
        '''
        查询资方业务编码
        '''
        sql = self.cursor.execute('SELECT fund_business_code from t_fund_info where fund_code = %s', fund_code)
        # 获取第所有数据
        results = self.cursor.fetchone()
        return results[0]
        #关闭数据库
        self.db.close()
if __name__ == '__main__':
    mysql = Mysql('fund_uat')
    res = mysql.query_route_pre_approval_result('6488a7c6319342d19cba8cc89aac1593')
    print(res)

