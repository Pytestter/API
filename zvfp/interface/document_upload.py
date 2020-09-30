'''
titile : 文件上传接口（固定数据）
author:张来明
date:20200813
version:python3.6.5
'''
import paramiko  # 用于调用scp命令
import datetime

from data.base_data import *
from data.create_document import *
from basic_method import *
from MongoClient import *
import time
import requests


class Document_upload:
    def __init__(self, thread_id, img_list, pdf_list):
        # 将文件上传到sftp
        self.file = FileUpload(thread_id, img_list, pdf_list)
        self.file.upload_files()
        self.headers = headers
        self.url = document_upload_url
        self.data = self.file.create_file_request_data()
        self.i = 0

    def document_upload_instruction(self):
        '''
        调用VFP文件上传接口
        '''
        print("=" * 30 + "开始调用文件上传接口" + "=" * 30)
        print("文件上传请求参数:",self.data)
        self.res = ApiMethod(self.url, self.data, self.headers).post_request()


    def document_result_qurey(self):
        '''
        调用文件上传查询接口
        '''
        query_url = self.url + self.res['data']['batchNo']
        self.i += 1
        print("第{}查询文件上传结果".format(self.i))
        time.sleep(1)
        res = requests.get(url=query_url, headers=self.headers)
        if res.json()['data'][0]['status'] == 'pending' and self.i < 10:
            return self.document_result_qurey()
        else:
            print(res.json())


if __name__ == '__main__':
    # 陪孩子参数
    thread_id = "MDUySiNWNS1fUCVIJSUjNEw4M18="
    img_list = ['01','02','37']  # 需要上传的图片
    pdf_list = ['07','22','72']  # 需要上传的文件
    document_upload = Document_upload(thread_id, img_list, pdf_list)
    # 文件上传
    document_upload.document_upload_instruction()
    # 调用文件上传查询
    document_upload.document_result_qurey()
