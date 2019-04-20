#coding=utf-8

'''a=6
b=5.99
c ='display'
d=9
print (a,b,c)
print(type(a))'''

'''
mass='let\'s go'
print(mass)
'''
'''time = input('please input number:')
print(time)

print(type(time))
list = [2,'box',3,'memery']

print(list)

a, b = eval(input('输入两个数，逗号隔开：'))
print (a,b)'''

'''a,b=input('请输入：').split()
print(a,b)'''

'''a,b =input('输入a,b空格隔开:').split()
#此时a,b为str型
a,b =map(int,input('输入a,b空格隔开:').split())
#此时a,b为int型'''

# a = input('请输入：')
# # print('the str is :',a)
# # print('the str is :%s'%a)
#
# b = input('please input :')
# print('the str is:%s, the number is:%s'%(a,b))

# tp = (1,'sd',4,'sdf')
# print (tp)
# print(type(tp))

# li = [2,'box',3,'memery']
# # print (li)
# # print(type(li))
#
# print(li[3])
#
# li = []
# for i in range(1,11):
#     li.append(i)
# print(li)
#
# print(li[3:6:1])
# print(li[6:9:])
# print(li[2:10:2])
# print(li[1:9:2])
# print(li[-5])
# print(li[3::])
#

# for j in range(0,10):
#     if j/2:
#         print('偶数为:',j)
#     else:
#         print('奇数为:',j)

# li = (1,2,3,4,5,6,7,8,9)
#
# print(li[-3])
# print(li[3:9:2])
#
# for i in range(0,10):
#     print (i)

# print (list(range(1,100)))
#
# a = input('plsease input:')
# b = int(a)
# print(a)
# print(type(a))

# a = [2,1,3,5,6,78]
# a.reverse()
# print (a)

# a=[23,536,578,5,346,3]
# a.sort()
# print(a)

#
# a = [3,2,76,34,9]
# print(sorted(a))
# print (a)

# a = [3,5,4,8,9,23]
# a.insert(2,10)
# print (a)

# a = [3,5,4,8,9,23]
# a.append(33)
# print(a)

# a = [3,2,'ds',45.5]
# b = ['sdf',23,45,34,'sd']
# a.extend(b)
# print (a)

# a = [3,2,'ds',45,5,45]
# a.pop(4)
# print(a)

# a = [2,44,354,46,12,4,3,2,3,2]
# a.remove(44)
# print(a)
# a = [2,44,354,46,12,4,3,2,3,2]
# a.count(2)
# print(a.count(2))

# print(max(a))
# print(min(a))
# print(len(a))
#
# print(a.index(44))
#
# del a[2]
# print(a)
#
# m = [11,13,5,7,0,56,23,34,72]
# print(max(m))
# print(min(m))
# print(len(m))
#
# print(m.index(56))
#
# m.append(7)
# print(m)
#
# del m[4]
# print (m)
#
# m.sort()
# m.reverse()
# print(m)
#
# b = [66,67,68]
# m.extend(b)
# print(m)
#
# b = [34,34,5,6,7,0,4,34,0]
# x = b.index(0)
# print(b.index(0))
#
# del b[x]
# print (b)

# s = [43,34,66,43,34,4646]
# m = set(s)   #转换为字典
# print(m)
#
# m=list(set(s))     #转换成列表
# print(m)

ox = {'a':10,'b':20,'c':30}

# print(ox)
# print(ox['b'])
# ox['d']=40
# print(ox)
# print(ox.keys())
# a=ox.values()
# print(a)
# print(ox.items())
# print(type(a))
# print(type(ox.items()))
#
# print(list(set(ox)))
# print(list(set(ox.keys())))
# print(list(ox.values()))
# b = list(set(ox.items()))
# print(b)

# a = int(input('please input a num:'))
# print(a)
#
# if a > 0:
#     print('yes')

# a = input('please input a num:')
# if int(a) > 0:
#     print('succes')
#
# elif (int(a)) == 0:
#     print('good')
# else:
#     print('failed')

# a = int(input('please input number:'))
#
# if a > 0:
#     a+=1
# else:
#     a-=1
# print (a)
#
# a = int(input('please input number:'))
#
# if a > 0:
#     a+=10
# elif a == 0:
#     a+=20
# else:
#     a-=1
# print (a)

# for i in range(5):
#     a = int(input('please input a number:'))
#     if a >90 and a <=100:
#         print('等级为：A')
#     elif a>80 and a<=90:
#         print('等级为：B')
#     elif a>70 and a<=80:
#         print('等级为：C')
#     elif a>60 and a<=70:
#         print('等级为：D')
#     elif a<=60 and a >= 0:
#         print('等级为：E')
#     else:
#         print('输入不合法')

# n=5
# while n>0:
#         a = int(input('please input a number:'))
#         if a >90 and a <=100:
#             print('等级为：A')
#         elif a>80 and a<=90:
#             print('等级为：B')
#         elif a>70 and a<=80:
#             print('等级为：C')
#         elif a>60 and a<=70:
#             print('等级为：D')
#         elif a<=60 and a >= 0:
#             print('等级为：E')
#         else:
#             print('输入不合法')
#         n = n-1

#练习：计算1+2+3+....+100

# sum = 0
# n=1
# while n<101:
#     sum = sum+n
#     n=n+1
# print(sum)
#
# s = 0
# for i in range(1,101):
#     # print (i)
#     s = s+i
# print (s)


# for i in [23,'sd',343,'sddd']:
#     print(i,'ok')
#
# for i in range(1,100,2):
#     print(i)

# for i in range(5):
#     if i ==3:
#         continue
#     print(i)

# for i in range(5):
#     if i ==3:
#         break
#     print(i)

# a=1
# for i in range(1,11):
#     a = a*i
# print (a)
#
# b = []
# for i in range(1,101):
#     if i%3 ==0:
#         b.append(i)
# print(b)


# m = [1,2,3,4,3,4,2,5,5,8,9,7]
# x = []
# for i in m:
#     for j  in m:
#         if i in j:
#             x.append(i)
#         else:
#             pass
# print (x)

# m = [1,2,3,4,3,4,2,5,5,8,9,7]
# a = list(set(m))
# print (a)


# a=1
# b=2
# for i in range(10):
#     sum=a+b
#     a=b
#     b=sum
#     print(sum)

# li = [1,2]
# a=0
# b=1
# for i in range(20):
#     sum = li[a]+li[b]
#     li.append(sum)
#     a+=1
#     b+=1
# print (li)


# li = []
# li2 = []
# for i in range(1,100):
#     for m in(1,i):
#         if i%m==0:
#             li.append(i)
#         while li.count()






