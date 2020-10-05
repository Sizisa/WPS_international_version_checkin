
import requests
import time
import json


def checkin(username,password,sckey):

    checkinFlag=False
    nowtime=int(time.time())

    #登录
    loginurl = "https://account.wps.com/p/signin"

    payload = 'cb=https%3A//www.wps.com/phone/&frame=1&from=mobilelogin&source=phone&account=s1@sgv5.uu.me&password=147258369.&keeponline=1'
    headers = {
    'Host': 'account.wps.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MI 9 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.89 Mobile Safari/537.36',
    'Origin': 'https://account.wps.com',
    'Referer': 'https://account.wps.com/mobilelogin?cb=https%3A%2F%2Fwww.wps.com%2Fphone%2F&frame=1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'uzone=US; ulocale=en-US; wps_sid=V02SSY1lNa5RLw0Z859ryY1S4_7mnGM00a9f6bc900070bdfae@usw2'
    }

    #response = requests.request("POST", url, headers=headers, data = payload)
    r=requests.post(url=loginurl,headers=headers,data=payload)
    if r.text.find('result')!=-1 and json.loads(r.text)['result']=='ok':
        print('登录返回cookies：')
        print(r.cookies)
        sid=r.cookies['wps_sid']
        print('登录成功，sid='+sid)
    else:
        #send(sckey,'WPS国际版签到失败','登录失败'+r.text)
        print(r.text)
        return (0,'登录失败')

    #检查今天是否签到
    checkUrl='https://micro.api.wps.com/checkin/everyDayCheckinInfo?wps_sid=%s'%sid
    dataJson={'client_time':nowtime,'timezone_offset':-480}
    
    r1=requests.post(url=checkUrl,json=dataJson).text
    result=json.loads(r1)
    print('检查签到返回信息'+r1)
    if result['code']==0 and result['is_checkined_today']==1:
        checkinFlag=True
        return (0,'error')

    #签到
    checkinUrl='https://micro.api.wps.com/task/DispatchTask?wps_sid=%s&token=AXEFASLFKSLP&client_time=%s&timezone_offset=-480'%(sid,nowtime)
    r=requests.get(url=checkinUrl).text
    print('签到返回信息'+r)


    #检查是否签到成功
    
    checkUrl='https://micro.api.wps.com/checkin/everyDayCheckinInfo?wps_sid=%s'%sid
    dataJson={'client_time':nowtime,'timezone_offset':-480}
    
    r1=requests.post(url=checkUrl,json=dataJson).text
    result=json.loads(r1)
    print('检查签到返回信息'+r1)
    if result['code']==0 and result['is_checkined_today']==1:
        return (1,str(result['consecutive_checkin_days']))
        #send(sckey,'WPS国际版签到成功','签到成功')
    else:
        return (0,r1)
        #send(sckey,'WPS国际版签到失败',r1)
        
    


