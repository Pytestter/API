'''
titile :通过源码方式，自动化安装Nginx
author:张来明
date:20200220
version:python3.6.5
'''
import os,sys
#权限检查
if os.getuid() !=0:
    print('当前用户不是root，请以root身份执行脚本')
    sys.exit(1)
#版本号的选择
def_var = '1.13.11'
var = input("请输入版本(默认{}):".format(def_var))
var = var or def_var
#安装目录的配置
def_path = 'usr/local/nginx'
path = input("请输入安装目录(默认{}):".format(def_path))
path = path or def_path
print(path)

#下载资源包
url =  'http://nginx.org/download/nginx-{}.tar.gz'.format(var)
cmd = 'wget ' +url
res = os.system(cmd)
if res !=0:
    print('下载失败')
    sys.exit(1)
#解压
cmd = 'tar -zxf nginx-{}.tar.gz'.format(var)
if os.system(cmd) !=0:
    print('解压失败')
    sys.exit(1)
#安装依赖
cmd = 'sudo apt-get install -y libpcre3 libpcre3-dev zlib1g-dev libssl-dev build-essential'
if os.system(cmd) !=0:
    print("安装失败")
    sys.exit(1)
#配置
cmd = 'cd nginx-{} && ./configure --prefix=/usr/local/nginx --with-http_ssl_module'.format(var)
if os.system(cmd) !=0:
    print('配置失败')
    sys.exit(1)

#编译
cmd = 'cd nginx-{} && make && make install'.format(var)
if os.system(cmd) !=0:
    print('编译失败')
    sys.exit(1)
print("安装成功")
