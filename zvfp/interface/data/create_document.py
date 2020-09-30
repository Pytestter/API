'''
创建上传文件的数据
author:张来明
date:20190830
version:python3.6.5
'''
import time
import datetime
from MongoClient import *
now = datetime.datetime.now()
data = str(int(time.time()))
date = now.strftime('%Y%m%d')  #当前日期
import paramiko  # 用于调用scp命令
HOST = '10.138.61.181'
PORT = 22
USERNAME = 'admin'
PASSWORD = 'admin123'

# 当天日期
TODAY = datetime.datetime.now().strftime('%Y%m%d')

class FileUpload:
    def __init__(self,threadId,img_list,pdf_list):
        self.fileId = data[4:10]
        self.threadId = threadId
        self.mongo = Mongo('fund_uat')
        self.res = self.mongo.query_loan_information_result(self.threadId)
        self.product_code = self.res['project_code']
        self.fundCode = self.res['fund_code']
        self.applyNo = "4180763"
        self.bid = self.res['bid']
        self.img_list = img_list
        self.pdf_list = pdf_list
        self.flist = self.img_list+self.pdf_list
        self.listFile = []
        self.wenjianpost_data = {}
    def upload_files(self):
        '''
        将文件上传到指定sftp
        '''
        transport = paramiko.Transport((HOST, PORT))  # 获取Transport实例
        transport.connect(username=USERNAME, password=PASSWORD)  # 建立连接
        sftp = paramiko.SFTPClient.from_transport(transport)
        PATH = 'upload/In/' + self.fundCode
        # 判断当前日期文件夹是否存在
        is_existence = True if TODAY in sftp.listdir(PATH) else False
        if not is_existence:
            # 创建文件夹
            sftp.mkdir(PATH + "/" + TODAY)
        if self.img_list != 0:
            for i in self.img_list:
                is_existence = True if "IMTP0000" + i in sftp.listdir(PATH + "/" + TODAY) else False
                if not is_existence:
                    sftp.mkdir(PATH + "/" + TODAY + "/" + "IMTP0000" + i)
                    # 上传
                    sftp.put("./data/img/file_" + i + ".jpg",
                             PATH + "/" + TODAY + "/" + "IMTP0000" + i + "/" + "file_" + i + ".jpg")
                    # 下载
                    # sftp.get("/home/rzbsftp/1586395726920.xlsx", "F:/222/1586395726920.xlsx")
                else:
                    sftp.put("./data/img/file_" + i + ".jpg",
                             PATH + "/" + TODAY + "/" + "IMTP0000" + i + "/" + "file_" + i + ".jpg")
        if self.pdf_list != 0:
            for i in self.pdf_list:
                is_existence = True if "IMTP0000" + i in sftp.listdir(PATH + "/" + TODAY) else False
                if not is_existence:
                    sftp.mkdir(PATH + "/" + TODAY + "/" + "IMTP0000" + i)
                    # 上传
                    sftp.put("./data/img/file_" + i + ".pdf",
                             PATH + "/" + TODAY + "/" + "IMTP0000" + i + "/" + "file_" + i + ".pdf")
                    # 下载
                    # sftp.get("/home/rzbsftp/1586395726920.xlsx", "F:/222/1586395726920.xlsx")
                else:
                    sftp.put("./data/img/file_" + i + ".pdf",
                             PATH + "/" + TODAY + "/" + "IMTP0000" + i + "/" + "file_" + i + ".pdf")
        sftp.close()
        transport.close()
    def create_file_request_data(self):
        '''
        创建文件上传接口的请求数据
        '''
        for i in self.flist:
            file = {}
            if i in self.img_list:
                file['fileType'] = 'IMTP0000'+i
                file['fileId'] =self.fileId+i
                file['extensionType'] = '.jpg'
                file['bid'] = self.bid
                file['fileName'] = "file_"+i
                file['remark'] = "picture_"+i
                file['remark'] = ""
                file['uploadDate'] = date
                file['vfpUrl'] ="/upload/In/"+self.fundCode+"/"+date+"/IMTP0000"+i+"/"+"file_"+i+".jpg"
                self.listFile.append(file)
            elif i in self.pdf_list:
                file['fileType'] = 'IMTP0000'+i
                file['fileId'] =self.fileId+i
                file['extensionType'] = '.pdf'
                file['bid'] = self.bid
                file['fileName'] = "file_"+i
                file['remark'] = "file_"+i
                file['remark'] = ""
                file['uploadDate'] = date
                file['vfpUrl'] ="/upload/In/"+self.fundCode+"/"+date+"/IMTP0000"+i+"/"+"file_"+i+".pdf"
                self.listFile.append(file)
        self.wenjianpost_data ={
          "batchSize": 1,
          "list": [{
            "transactionId": "zlmwenjianpost"+data,
            "threadId": self.threadId,
            "fundCode": self.fundCode,
            "bid": self.bid,
            "applyNo":self.applyNo,
            "productCode":self.product_code,
            "listFile": self.listFile
             }]}
        return self.wenjianpost_data

if __name__ == '__main__':
    #文件上传测试
    thread_id = 'IyM3TCUtNCM0MF9S'
    img_list = ['01','02','03']
    pdf_list = ['07']
    file_upload = FileUpload(thread_id,img_list,pdf_list)
    file_upload.upload_files()

