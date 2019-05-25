#coding=utf-8
#__author__= 'jws'

from ddt import ddt,data,unpack
import unittest
from day4 import Myadd
@ddt
class Mytest(unittest.TestCase):

    def setUp(self):
        print('--init--')

    @data('hello')
    def test_case1(self,value):
        print(value)
        self.assertEqual(value,2)
    @data(2,3,4)
    def test_case2(self,val):
        self.assertEqual(val,2)
        print(val)
        print('--ok--')

    def tearDown(self):
        print('--clear--')

if __name__ == '__main__':
    unittest.main()