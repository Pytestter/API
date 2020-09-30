'''
titile :消息队列中的应用
author:张来明
date:20200220
version:python3.6.5
'''
from backend import send_sms

#保存数据库
def save():
    print("sava")


save()
#delay是celery.task所提供的方法
send_sms.delay()