#coding=utf-8
#__author__= 'jws'

import requests

urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'jingwenshuai','password':'123456'}

r = requests.post(url=urlstr,data=data)

htm = r.text
if r.status_code == 200:
    print('success!')
else:
    print('false')
if r.json()['data']['username']=='jingwenshuai':
    print('登陆成功')
else:
    print('登陆失败')
