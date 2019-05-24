#coding=utf-8
#__author__= 'jws'

import re
#在起始位置匹配
# print(re.match('www','www.runboob.com').span())
#
# #不再起始位置匹配
# print(re.match('www','www.runboob.com'))

res = re.search('www','www.baidu.www.com')
print(res)
print(res.group(0))