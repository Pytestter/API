'''
titile :监控内存和CPU，并发送邮件和微信消息
author:张来明
date:20200220
version:python3.6.5
'''
import psutil
import time
class Monitor():
    #保存CPU使用率占比
    cpu_list = []
    #监控内存
    @classmethod
    def mem(cls,max):
        #获取内存使用率
        res = psutil.virtual_memory().percent
        if res > max:
            cls.send_msg("内存使用率为{}，超过了{}%，请关注！".format(res,max))

    #监控CPU
    @classmethod
    def cpu(cls,max):
        #获取CPU使用率占比
        res = psutil.cpu_percent(interval=1)
        cls.cpu_list.append(res)
        print(cls.cpu_list)
        if len(cls.cpu_list) >=3:
            avg = sum(cls.cpu_list)/len(cls.cpu_list)
            if avg > max:
                cls.send_msg("CPU平均使用率为{}，超过了{}%，请关注！".format(avg, max))
            cls.cpu_list.pop(0)

    #发送消息
    @classmethod
    def send_msg(cls,content):
        cls.send_mail(content)
        cls.weChat(content)
        print(content)

    #发送邮件
    @classmethod
    def send_mail(cls,content):
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr
        #发件人昵称
        nickname = '监控程序'
        sender = 'zhanglm028@qq.com'
        password = 'wsvuqamwkwhobecf'
        reverser = 'laiming007@foxmail.com'
        #内容为test,已HTML的形式发送
        msg = MIMEText(content,'html','utf-8')
        msg['From'] = formataddr([nickname,sender])
        #标题
        msg['subject'] = '自动报警'
        server = smtplib.SMTP_SSL('smtp.qq.com',465)
        try:
            server.login(sender,password)
            server.sendmail(sender,[reverser],msg.as_string())
        except Exception as ex:
            print(ex)
        finally:
            server.quit()
    #发送微信消息
    @classmethod
    def weChat(cls,content):
        from wechatpy import WeChatClient
        import datetime
        #传入appid 和APPsecret
        client = WeChatClient('wx66eaadc2f71745f6','9b392a3a846d50d23ebb1a52c8905bf3')
        #模板id
        template_id = 'CYEFb6UQZbxvJZ2j4avVDTfXxEtlXHq-ToKx0pI2A7g'
        user_id = 'ozqXivx-kJgGrqict_LmlG9GY2wU'
        #对占位符进行声明
        data = {
            'msg': {"value": content, "color": "#173177"},
            'time': {"value": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "color": "#173177"},
        }
        client.message.send_template(user_id,template_id,data)

while True:
    Monitor.mem(50)
    Monitor.cpu(20)
    time.sleep(5)

