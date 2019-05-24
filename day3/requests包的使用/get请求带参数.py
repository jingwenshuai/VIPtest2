#coding=utf-8
#__author__= 'jws'

import requests

urlstr = 'https://www.wanandroid.com/article/query'

param = {'k':'android'}

r = requests.get(url=urlstr,params=param)
print(r.text)
print(r.status_code)