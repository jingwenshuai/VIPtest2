# #coding=utf-8
# #__author__= 'jws'
#
# #已知异常
# def cala(a,b):
#     try:
#         print(a/b)
#     #已知异常
#     except ZeroDivisionError:
#         print('除数不能为0')
# a = int(input('-'))
# b = int(input('-'))
# cala(a,b)
#
# #------未知异常
# #except NameError as e:抛出异常
# def cala(a,b):
#     try:
#         print(a/b)
#     #未知异常
#     except BaseException:
#         print('除数不能为0')
# a = int(input('-'))
# b = int(input('-'))
# cala(a,b)
#
# #------多重异常
# def cala(a,b):
#     try:
#         print(a/b)
#     except NameError:
#         print('对象未声明')
#     except BaseException:
#         print('除数不能为0')
# a = int(input('-'))
# b = int(input('-'))
# cala(a,b)
#
# #------最终处理---不管有没有抛出异常都会执行finally
# def cala(a,b):
#     try:
#         print(a/b)
#     except NameError:
#         print('对象未声明')
#     except BaseException:
#         print('除数不能为0')
#     finally:
#         print('程序执行完毕！')
# a = int(input('-'))
# b = int(input('-'))
# cala(a,b)


#---抛出异常----异常必须为exception的子类
# raise TypeError('类型错误！')

#-----正常情况下执行else
# def cala(a,b):
#     try:
#         print(a/b)
#     except NameError:
#         print('对象未声明')
#     except BaseException:
#         print('除数不能为0')
#     else:
#         print('程序执行完毕！')
# a = int(input('-'))
# b = int(input('-'))
# cala(a,b)

def fun0(b):
    try :
        print(a+b)
        c = 4
        print(b/c)
    except NameError as e:
        print(e)
        print('a变量未声明')
    except TypeError:
        print('b的类型错误')
    finally:
        print('程序执行完毕')
b = input('请输入第一个数：')
fun0(b)