import checkin
import os
import requests
  
def msgFormat(i,username,num,flag):
    string='----\n'\
        +'* 用户'+str(i)+'\n'\
        +'\t> `用户名：'+username+'`\n'\
        +'\t\n'\
        +'\t>`已签到 '+str(num)+' 天`\n'\
        +'\t\n'\
        +'\t>`今天已签到：'+flag+'`\n'\
        +'\t\n'
    return string
    

def send(sckey,title,msg):
    url='http://sc.ftqq.com/%s.send'%(sckey)
    data={'text':title,'desp':msg}
    r=requests.post(url=url,data=data)
    print('server酱返回信息：'+r.text)


def wpsCheckin(usernames,password,sckey):
    string=''
    usernames=usernames.split('#')
    print('------------WPS国际版开始签到------------')
    for i,username in enumerate(usernames):
        print('===========为第'+str(i+1)+'个用户签到，用户名：'+username+'============')
        (flag,num)=checkin.checkin(username,password,sckey)
        if flag==1:
            string+=msgFormat(i+1,username,num,'是')
        elif flag==0:
            string+=msgFormat(i+1,username,num,'否')
        print('========================================')
    send(sckey,'WPS国际版签到通知',string)

if __name__ == "__main__":
    username = os.environ['username']
    password = os.environ['password']
    sckey = os.environ['sckey']
    
    
    wpsCheckin(username,password,sckey)