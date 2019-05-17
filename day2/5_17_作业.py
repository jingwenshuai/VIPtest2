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

class soldier:

    def __init__(self,name):
        #定义属性：
        # 1.姓名
        self.name = name
        # 2.枪
        self.gun = None
    #开枪方法
    def fire(self):
        #判断是否有枪
        if self.gun is None:
            print('[%s]还没有枪！'%self.name)
            return
        print('开枪吧%s'%self.name)
        #让枪装子弹，调用添加子弹方法
        self.gun.add_zd(10)

        #让枪射击，调用开枪方法
        self.gun.shoot()

#创建一个枪的类，包含枪的类型和子弹数量两个属性
#枪有两个方法，一个添加子弹方法，一个开枪方法

class Gun:

    def __init__(self,xh):
        #枪的型号
        self.xh = xh
        #子弹的数量
        self.zd_count = 0

    #添加子弹
    def add_zd(self,count):
        self.zd_count += count

    #开枪射击
    def shoot(self):
        #判断子弹数量
        if self.zd_count <=0:
            print("[%s]没有子弹了!"%self.xh)
            return
        self.zd_count -=1
        print('[%s] biu biu biu...剩余[%d]颗子弹'%(self.xh,self.zd_count))

#创建枪对象
ak47 = Gun('AK47')
#创建瑞恩
ruien = soldier('瑞恩')
#给瑞恩枪
ruien.gun = ak47
#开火
ruien.fire()





