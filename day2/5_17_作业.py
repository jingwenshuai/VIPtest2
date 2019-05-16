#coding=utf-8
#__author__= 'jws'

'''
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
'''
#创建一个士兵类，创建init方法有name属性，gun属性
#创建一个开火方法，动作：扣动扳机
#创建一个
class soldier:

    def __init__(self,name,gun):
        self.name = name
        self.gun = gun

    def