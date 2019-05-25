#coding=utf-8
#__author__= 'jws'

import unittest
from unittest_test import Mysum

class Mytest(unittest.TestCase):

    def setUp(self):
        print('----初始化测试环境')

    def test_sum(self):
        # x = int(input('x-->>'))
        # y = int(input('y-->>'))
        re = Mysum.sum(1,2)
        if re==3:
            print('测试通过')
        else:
            print('测试失败')
    def test_fun1(self):
        r = Mysum.sum(4,5)
        print(r)

    def tearDown(self):
        print('---清理测试环境')

if __name__ == '__main__':
    #main方法会自动执行这个类中所有以test开头的方法
    # unittest.main()

    #手动添加，实例化测试套件，先实例化一个TestSuite类
    suite = unittest.TestSuite()
    #调用addTest方法想测试套件中添加测试方法
    suite.addTest(Mytest("test_fun1"))

    #运行测试套件：1，实例化测试运行类
    runer = unittest.TextTestRunner()
    runer.run(suite)


