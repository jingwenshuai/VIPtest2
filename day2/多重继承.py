#coding=utf-8
#__author__= 'jws'

class Base(object):
    def test(self):
        print("------base")
class A(Base):
    def test(self):
        print("-----test1")
class B(Base):
    def test(self):
        print("------test2")
class C(A,B):
    pass
c = C()
c.test()
# c.test1()
# c.test2()