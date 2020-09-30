'''
titile : 基础方法类
author:张来明
date:20190731
version:python3.6.5
'''
import sys
import time
import json
import requests

def read_content(self,path):
    #读取指定目录文件的内容,path为文件目录
    file = open(path,"r",encoding='utf-8')
    content = file.read()      #读取出来的内容Wie字符串类型
    print("文件内容为：",content)
    #将读取内容转化为列表
    list = eval(content)
    print(list[0]+" "+list[1]+" "+list[2])

def write_to_file(base_path,name,content):
    '''
    创建一个以当前时间为命名的txt文件，并写入内容
    '''
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    path = base_path+now+"-"+name+".txt"
    with open(path,'a',encoding="utf-8") as fp:
        fp.write(json.dumps(content,indent=4,ensure_ascii=False))
        fp.close()
def dict_to_json(self,data):
    #字典转化为json字符串
    return json.dumps(data)
def json_to_dict(self,data):
    #json字符串转化为字典
    return json.loads(data)


# 定义一个API类
class ApiMethod():
    def __init__(self, url, data, header=None):
        self.url = url
        self.data = data
        self.header = header
    # post请求
    def post_request(self):
        if self.header != None:
            res = requests.post(url=self.url, json=self.data, headers=self.header, verify=False)
            print("请求状态码为:", res.status_code)
            print("响应报文:", res.text)
        else:
            res = requests.post(url=self.url, json=self.data, verify=False)
            print("请求状态码为:", res.status_code)
            print("响应报文:", res.text)
        return res.json()

    # post 返回
    def post_respond(self):
        post_res = self.post_request()
        return post_res
    def get_request(self):
        if self.header != None:
            res = requests.get(url=self.url, json=self.data, headers=self.header, verify=False)
            print("请求状态码为:", res.status_code)
            print("响应报文:", res.text)
        else:
            res = requests.get(url=self.url, json=self.data, verify=False)
            print("请求状态码为:", res.status_code)
            print("响应报文:", res.text)
        return res.json()

    def get_respond(self):
        get_res = self.get_request()
        return get_res

def send_mail(content):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    # 发件人昵称
    nickname = '张来明'
    sender = 'zhanglm028@qq.com'
    password = 'wsvuqamwkwhobecf'
    reverser = 'laiming007@foxmail.com,zhanglaiming@vcredit.com'
    # 内容为test,已HTML的形式发送
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = formataddr([nickname, sender])
    # 标题
    msg['subject'] = '测试报告'
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    try:
        server.login(sender, password)
        server.sendmail(sender, reverser.split(','),msg.as_string())
    except Exception as ex:
        print(ex)
    finally:
        server.quit()
def test():
    print("hello world!")
if __name__=='__main__':
   pass