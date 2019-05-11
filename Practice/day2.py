#coding=utf-8

#函数
# a = int(input('输入第一个值:'))
# b = int(input('输入第二个值:'))
# def calc():
#     c = a+b
#     print(c)
# calc()

# def add_end():
#     L = []
#     L.append('end')
#     return L
# print(add_end())
# print(add_end())

# def add_end(L = []):
#     L.append('end')
#     return L
# print(add_end())
# print(add_end())
# print(add_end())
#
# def calc(*numbers):
#     print(*numbers)
#     print(numbers)
#     sum = 0
#     for n in numbers:
#         sum+=n
#     return sum
#
# print(calc(1,2))

# def calc(*args):
#     print(*args)
#     print(args,type(args))
#     for i in args:
#         print('传入的值分别为:',i)
#
# #可变参数
# m = [1,2,3]
# calc(*m)
# calc(1,2,3)
# #传参为引用时，需加*号

# def person(name,age,**kwargs):
#     print ('name',name,'age',age,kwargs,type(kwargs))
#
#
# person('xh',18,sex='girl')
# person('ss',44)

#练习：设计一个计算器，输入两个数，自动实现加减乘除（进阶：根据用户输入的计算符号计算结果）

# def cala():
#     a = int(input('输入第一个数：'))
#     b = int(input('输入第二个数：'))
#     # c = input('输入运算符号')
#     # sum = acb
#     x = a + b
#     y = a - b
#     z = a * b
#     m = a/b
#
#     print('a+b =',x)
#     print('a-b =',y)
#     print('a*b =',z)
#     print('a/b =',m)
#
# cala()


def cala():
    a = int(input('输入第一个数：'))
    b = int(input('输入第二个数：'))
    c = input('输入运算符号:')
    if c == '+':
        result = a + b
        print('a+b =',result)
    elif c == '-':
        result = a - b
        print('a-b =', result)
    elif c == '*':
        result = a*b
        print('a*b =', result)
    elif c =='/':
        result = a/b
        print('a/b =', result)
    else:
        print('输入不合法！')
cala()