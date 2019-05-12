# #coding=utf-8
# #__author__= 'jws'
#
# f = open('C:\D\VIPtest2\data.txt','r')
#
# #read()读取文件全部内容
# # print(f.read())
#
# # #读取指定长度字节的数据
# # print(f.read(4))
#
# #读取整行
# print(f.readline())
#
# #读取所有行
# print(f.readlines())
#
# with open('C:\D\VIPtest2\data.txt','r') as f:
#     print(f.read())
# f.close()
#-----------------------------------------#

# f = open('C:\D\VIPtest2\data.txt', 'r+')
# f.write('hello world!')
# #控制指针位置
# f.seek(0)
# print(f.read())
# f.close()

#------------------------------------------#
#练习：
#--------read()方法读出来的是一个str类型
#--------readlines()方法读出来的是一个list类型

# with open('C:\D\VIPtest2\data.txt') as f:
#     res = f.read()
#     print(res)
#     print(type(res))
#     f.seek(0)
#     oo = f.readlines()
#     print('------------')
#     print(oo)
#     print(type(oo))
#     m = res.replace("\n",",")
#     L = []
#     x = res.split(',')
#     # print (x)
#     for a in oo:
#         if a.isdigit():
#             L.append(a)
#         f.close()
#         L.reverse()
#     print(L)
'''
with open('C:\D\VIPtest2\data.txt','r+') as f:
    print(f.read())
    print(type(f.read()))
    print('----------------------------------')
    f.seek(0)
    print(f.readlines())
    print(type(f.readlines()))
    print('----------------------------------')
    f.seek(0)
    print(f.readline())
    print(type(f.readline()))
'''

with open('C:\D\VIPtest2\data.txt','r+') as f:
    res = f.read()
    print(res)

    #字符串替换，将空格替换为逗号
    res = res.replace('\n',',')
    print('res为：',res)

    #字符串分割，将字符串以逗号分隔成为一个列表
    m = res.split(',')
    print('m为：',m)
    P = []
    for i in m:
        if i.isdigit():
            P.append(i)
    #sort()排序方法直接改变列表
    P.sort()
    print(P)