import checkin
import os

def wpsCheckin(sid,sckey):
    print('WPS国际版开始签到')
    checkin.checkin(sid,sckey)

if __name__ == "__main__":
    sid = os.environ['sid']
    sckey = os.environ['sckey']
    wpsCheckin(sid,sckey)