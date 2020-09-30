'''
titile :读取缓存中的数据
author:张来明
date:20200220
version:python3.6.5
'''
import pymysql
import memcache

def get_data():
    mc = memcache.Client(['127.0.0.1:11211'])
    cache_key = 'name_list'
    res = mc.get(cache_key)
    if res is not None:
        return res

    print("=======db==============")
    conn = pymysql.Connect(host='localhost',user='root',passwd='123456',database='test',charset='utf8')
    cursor = conn.cursor()
    sql = 'select * from t1'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    mc.set(cache_key,data,10)
    return data

name_list = get_data()
print(name_list)