from fabric.api import *
import datetime
env.user = 'root'
env.hosts = ['192.168.88.130','192.168.88.132']
def pack():
    local('rm -rf temp.tar.gz')
    local('cd project1 && git pull origin master')
    local('cd project1 && rm -r myweb/')
    local('cd project1 && unzip myweb.zip')
    local('cd project1 && tar -czf ../temp.tar.gz ./myweb')
def deploy():
    remote_temp_tar = '/tmp/temp.tar.gz'
    run('rm -rf ' + remote_temp_tar)
    put('temp.tar.gz',remote_temp_tar)

    tag = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    remote_dist_dir = '/data/deploy/project@' + tag
    run('mkdir -p '+remote_dist_dir)

    with cd(remote_dist_dir):
        run('tar -zxf '+remote_temp_tar)
    
    run('mkdir -p /data/webroot')
    link = '/data/webroot/project1'
    run('rm -rf '+ link)
    run('ln -s %s %s'%(remote_dist_dir,link) )
