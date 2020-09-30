'''
titile :消费队列中堆积的消息
author:张来明
date:20200220
version:python3.6.5
'''
import pika
import time

# 用户名与密码
user_pwd = pika.PlainCredentials('jack', '123456')

# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.88.130', credentials=user_pwd))

# 在连接上创建一个信道
channel = connection.channel()

# 定义回调函数，接收消息
def callback(ch, method, properties, body):
    print(" [消费者] %r:%r" % (method.routing_key, body))

    time.sleep(3)  # 模拟耗时

    ch.basic_ack(delivery_tag=method.delivery_tag)

# 再同一时刻，不要发送超过1条消息给一个工作者（worker），直到它已经处理了上一条消息并且作出了响应
channel.basic_qos(prefetch_count=1)  #消费者(worker)轮流消费消息

#consumer_tag = channel.basic_consume(callback,queue='queue1')
consumer_tag = channel.basic_consume('queue1',callback, False)

# 循环等待接收消息
channel.start_consuming()

connection.close()