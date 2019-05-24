#coding=utf-8
#__author__= 'jws'

import requests
#发送post请求
urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'jingwenshuai','password':'123456'}

r = requests.post(urlstr,data=data)
print(r.text)
print(r.status_code)
print(type(r.json()))
#通过字典dict-key来访问对应的值
print(r.json()['data']['username'])