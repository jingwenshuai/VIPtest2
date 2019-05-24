#coding=utf-8
#__author__= 'jws'

#导入requests包
import requests

# #发送get请求
urlstr = 'https://www.wanandroid.com/blog/show/2'

#发送请求
r = requests.get(url=urlstr)
print(r.headers)
# 打印结果
# print(r.text)

# urlstr = 'https://www.wanandroid.com/article/query'
#
# param = {'k':'android'}
# r = requests.get(url=urlstr,params=param)
# print(r.text)
# print(r.status_code)

#发送post请求
# urlstr = 'https://www.wanandroid.com/user/login'
#
# data = {'username':'jingwenshuai','password':'123456'}
#
# r = requests.post(urlstr,data=data)
# print(r.text)
# print(r.status_code)