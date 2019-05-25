#coding=utf-8
#__author__= 'jws'

import unittest
from unittest_test import Mysum

class Mytest(unittest.TestCase):

    def setUp(self):
        print('----初始化测试环境')

    def test_sum(self):
        x = int(input('x-->>'))
        y = int(input('y-->>'))
        re = Mysum.sum(x,y)
        if re==3:
            print('测试通过')
        else:
            print('测试失败')

    def tearDown(self):
        print('---清理测试环境')

if __name__ == '__main__':
    unittest.main()
