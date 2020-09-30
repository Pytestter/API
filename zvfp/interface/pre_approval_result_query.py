'''
输入token，查询预审批数据
分别包括route_auth_token、pre_approval_instruction和
'''
from interface.MongoClient import Mongo
from interface.MysqlClient import Mysql

class Query:
    def __init__(self,db,token):
        self.db = db
        self.token = token
        self.mysql = Mysql(self.db)
        self.mongo = Mongo(self.db)
    def query_approval_result(self):
        '''同时查询MySQL和MongoDB中的预审批结果'''
        #查询MySQL中的预审批结果
        thread_ids = self.mysql.query_route_pre_approval_result(self.token)
        for thread_id in thread_ids:
            #通过thread_id 查询MongoDB中的数据
            id = self.mongo.query_pre_approval_result(thread_id)['_id']
            print("查询资方的instruction_id为:{}".format(id))
            #通过id查询资方交互表的instruction_id
            self.mongo.query_fund_result(str(id))


while True:
    if __name__ == '__main__':
        db_default = 'fund_uat'
        db = input("请选择环境(默认uat,输入2切换为sit2,输入q退出):")
        if db == '':
            pass
        elif db == 'q':
            break
        elif db == '2':
            db = 'fund_sit2'
        else:
            print("输入错误，请重新输入！")
            continue
        db = db or db_default
        token = input("请输入token:")
        query = Query(db,token)
        query.query_approval_result()





