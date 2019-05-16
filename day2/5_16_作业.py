#coding=utf-8
#__author__= 'jws'

'''
3，摆放家具
需求：
1）房子有户型，总面积和家具名称列表
新房子没有任何家具
2）家具有名字和占地面积。其中：
床：占4平米
衣柜：占2平米
餐桌：占1
.5
平米
3）将以上三件家具添加到房子中
4）打印房子时，要求输出：户型，总面积，剩余面积，家具名称列表
'''

#1、定义一个房子类，属性有：户型、总面积、剩余面积、家具名称列表
#2、定义一个房子类，属性有：家具，占地面积

class Home:

    def __init__(self,home_type,area):
        self.home_type = home_type
        self.area = area
        self.freearea = area  #初始值等于总面积
        self.jiaju = []

    def __str__(self):
        #输出：户型，总面积，剩余面积，家具名称列表
        return (' 户型：%s \n 总面积：%.2f \n 剩余面积：%.2f \n 家具名 %s'
                %(self.home_type,self.area,self.freearea,self.jiaju))

    def add_jiaju(self,itm):
        print('要添加%s'%itm)
        #判断家具的面积
        if itm.area > self.freearea:
            print('%s的面积太大，无法添加！'%(itm.name))
            return
        #将家具的名称添加到列表
        self.jiaju.append(itm.name)
        #计算剩余面积
        self.freearea -=itm.area

class jiaju():

    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[ %s ]：占地 [ %.2f ] 平米"%(self.name,self.area)

#创建家具
bed = jiaju("床",4)
chest = jiaju('衣柜',2)
table = jiaju('餐桌',1.5)
print('bed：',bed)
print('bed：',bed.name)
print('bed：',bed.area)
print(chest)
print(table)

#创建房子
myhome = Home('三室一厅',100)
myhome.add_jiaju(bed)
myhome.add_jiaju(chest)
myhome.add_jiaju(table)
print(myhome)