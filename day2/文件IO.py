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

with open('C:\D\VIPtest2\data.txt') as f:
    res = f.read()
    m = res.replace("\n",",")
    L = []
    x = m.split(' ')
    print (x)
    for i in x:
        for a in i:
            print(a)
            if a.isdigit():
                L.append(a)
            else:
                continue
            f.close()
        L.reverse()
        print()

