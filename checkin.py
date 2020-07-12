
import requests
import time
import json

def send(sckey,title,msg):
    url='http://sc.ftqq.com/%s.send'%(sckey)
    data={'text':title,'desp':msg}
    r=requests.post(url=url,data=data)
    print('server酱返回信息：'+r.text)

def checkin(sid,sckey):
    nowtime=int(time.time())


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
        send(sckey,'WPS国际版签到成功','签到成功')
    else:
        send(sckey,'WPS国际版签到失败',r1)
        
    


