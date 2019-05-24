#coding=utf-8
#__author__= 'jws'

import requests

urlstr = 'https://www.wanandroid.com/blog/show/2'

header = {'User-Agent':'Mozilla/7.0'}

#发送请求
r = requests.get(url=urlstr,headers=header)
print(r.headers)
print(type(r.headers))
