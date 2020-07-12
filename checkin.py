
import requests
import time
import json








def checkin(username,password,sckey):
    nowtime=int(time.time())

    #登录
    loginUrl='https://account.wps.com/p/signin'
    headers={'Referer':'https://account.wps.com/framelogin?cb=https%3A%2F%2Fwww.wps.com%2Fmaca'}
    data={'cb': 'https://www.wps.com/mac/','from': 'login','source': 'ios','account': username,'password': password,'keeponline': 1}
    r=requests.post(url=loginUrl,headers=headers,data=data)
    if r.text.find('result')!=-1 and json.loads(r.text)['result']=='ok':
        print('登录返回cookies：')
        print(r.cookies)
        sid=r.cookies['wps_sid']
        print('登录成功，sid='+sid)
    else:
        #send(sckey,'WPS国际版签到失败','登录失败'+r.text)
        return (0,'登录失败')


    #签到
    checkinUrl='https://micro.api.wps.com/task/DispatchTask?wps_sid=%s&token=AXEFASLFKSLP&client_time=%s'%(sid,nowtime)
    r=requests.get(url=checkinUrl).text
    print('签到返回信息'+r)


    #检查是否签到成功
    #sid=f8953d8cf22c595e93b9eeb86cfa8ea29f67864900070bdfae@usw2
    checkUrl='https://micro.api.wps.com/checkin/everyDayCheckinInfo?wps_sid=%s'%sid
    dataJson={'client_time':nowtime}
    
    r1=requests.post(url=checkUrl,json=dataJson).text
    result=json.loads(r1)
    print('检查签到返回信息'+r1)
    if result['code']==0 and result['is_checkined_today']==1:
        return (1,str(result['consecutive_checkin_days']))
        #send(sckey,'WPS国际版签到成功','签到成功')
    else:
        return (0,r1)
        #send(sckey,'WPS国际版签到失败',r1)
        
    


