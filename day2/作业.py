#coding=utf-8
#__author__= 'jws'
'''
Python练习题：
1、打印小猫爱吃鱼，小猫要喝水
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
 
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
'''


# 1、打印小猫爱吃鱼，小猫要喝水
# class Animal():
#
#     def __init__(self,name,food,wt):
#         self.name = name
#         self.food = food
#         self.wt = wt
#
#     def cat(self):
#         print("%s爱吃%s,%s要喝%s"%(self.name,self.food,self.name,self.wt))
#
# Animal('小猫','鱼','水').cat()

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤

# class Person:
#
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#     def __str__(self):
#         return "我的名字叫[%s],体重是[%.2f]公斤"%(self.name,self.weight)
#
#     def run(self):
#         print("[%s]爱跑步，爱吃东西" %(self.name))
#         print("[%s]每次跑步会减肥0.5公斤" %(self.name))
#         self.weight -=0.5
#
#     def eat(self):
#         print("[%s]每次吃东西，体重会增加1公斤"%(self.name))
#         self.weight +=1
# xiaoming = Person('小明',75.0)
# xiaoming.run()
# print(xiaoming)
# xiaoming.eat()
# print(xiaoming)
# print('-------------------------')
# xiaoming = Person('小美',45.0)
# xiaoming.run()
# print(xiaoming)
# xiaoming.eat()
# print(xiaoming)


# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

class Home:         #创建房子类

    def __init__(self):
        self.name = name


class Hose():  #创建家具类

    def __init__(self):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]：占地[%.2f]"%(self.name,self.area)
#
