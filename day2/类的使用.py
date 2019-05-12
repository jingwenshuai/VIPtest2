#coding=utf-8
#__author__= 'jws'
# class Student():
#     #类属性
#     name = '小明'
#
#     def eat(self,food):
#         print("%s吃%s" % (self.name,food))
# a = Student()
# a.eat('apple')

class Student():
    #初始化方法，类中必须存在的且在实例化过程中自动被调用的方法
    def __init__(self,nm):
        self.name = nm
    def study(self,kc):
        print("%s学习%s课程" % (self.name,kc))
a = Student('小明')
a.study('数学')

class Student():
    #初始化方法，类中必须存在的且在实例化过程中自动被调用的方法
    def __init__(self,xh):
        self.xh = xh
    def study(self,kc):
        print("学号为%s的学生，学习%s课程" % (self.xh,kc))
a = Student('007')
a.study('数学')
