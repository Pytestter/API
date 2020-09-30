from string import  Template
import psutil
import os,sys
import datetime

#读取配置文件内容
with open('./nginx.config.tpl') as f:
    lines = f.readlines()
    lines = "".join(lines)
#获取CPU核心数
cpu = psutil.cpu_count()
params = {
    'worker_processes':cpu,
    'listen':8001,
    'server_name':'localhost',
    'root':'/data/webroot',
}
#替换模板中的占位符
tpl = Template(lines)
res = tpl.substitute(**params)
#print(res)
#建模版替换后的内容写入到一个零时文件中
temp = '/usr/local/nginx/conf/nginx.conf.temp'
with open(temp,'w') as f:
    f.write(res)
#检查配置文件是否合法
cmd = '/usr/local/nginx/sbin/nginx -c {} -t'.format(temp)
if os.system(cmd) !=0:
    print("配置文件内容有误")
    sys.exit(1)
#备份配置文件
config_file = '/usr/local/nginx/conf/nginx.conf'
if os.path.exists(config_file):
    os.rename(config_file,config_file+datetime.datetime.now().strftime('@%Y%m%d%H%M%S'))
#将我们上传的文件命名为配置文件
os.rename(temp,config_file)

#重新启动Nginx服务
if os.system('/usr/local/nginx/sbin/nginx -s reload') !=0:
    print('重新加载配置文件失败')
    sys.exit(1)
