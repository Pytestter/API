import time
from celery import Celery

celery = Celery(broker='amqp://jack:123456@192.168.88.130:5672/')
#发送短信(消耗时间)
@celery.task
def send_sms():
    time.sleep(5)
    print("sms")
