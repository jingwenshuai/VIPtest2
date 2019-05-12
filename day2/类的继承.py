#coding=utf-8
#__author__= 'jws'

# class Animal:
#
#     def eat(self):
#         print('旺财吃东西！')
#
#     def drink(self):
#         print('旺财喝水！')
#
# class Dog(Animal):


# class Person:
#     gh = 'dd'
#     def ls(self,xb,kc):
#         print('%s为%s的老师，教%s课程！' % (self.gh,xb,kc))
#     def gz(self,xb,gs,mn):
#         print('%s为%s的老师，在%s上班，一月工资%s!' % (self.gh,xb,gs,mn))
#
# class Teacher(Person):
#     pass
#
# a = Teacher()
# a.ls('男','英语')
# a.gz('男','阿里','1000$')
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print('吃东西')


# class Teacher(Person):
#     def __init__(self,gh):
#         self.gh = gh
#     def teach(self,course):
#         print('工号为：%s的老师教%s课程' % (self.gh,course))
#         print(self.eat())
#         print(Person.eat(self))
# a = Teacher('007')
# a.teach('英语')

#第一步：继承谁，类中的括号就写谁
#第二步：继承后，子类就具有父类的所有属性和方法，但是父类不能具备子类的属性和方法
#第三步：如果父类中没有子类需要的方法，可以在子类中自行定义
#注意：实例化和调用时要区分是否需要传参



