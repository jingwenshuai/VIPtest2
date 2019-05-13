#coding=utf-8
#__author__= 'jws'

with open('C:\D\VIPtest2\day2\data.txt','r+') as f:
    res = f.read()
    print(res)

    #字符串替换，将空格替换为逗号
    res = res.replace('\n',',')
    print('res为：',res)

    #字符串分割，将字符串以逗号分隔成为一个列表
    m = res.split(',')
    print('m为：',m)

    #取出数字部分
    P = []
    for i in m:
        if i.isdigit():
            P.append(i)
    #冒泡排序
    cd = len(P)
    while cd > 0:
        for i in range(len(P)-1):
            if P[i] > P[i+1]:
                P[i],P[i+1] = P[i+1],P[i]
        cd -=1
    print(P)
