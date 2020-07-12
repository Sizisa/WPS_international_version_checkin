import checkin
import os

def wpsCheckin(username,password,sckey):
    print('WPS国际版开始签到')
    checkin.checkin(username,password,sckey)

if __name__ == "__main__":
    username = os.environ['username']
    password = os.environ['password']
    sckey = os.environ['sckey']
    wpsCheckin(username,password,sckey)