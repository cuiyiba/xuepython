'''
    unittest
    1.子类继承TestCase
    2.写用例，test开头
'''
from unittest import TestCase

from Calc import Calc


class TestCalc (TestCase):

    def testAdd1(self):
        a = 6
        b = 5
        c = 11

        calc = Calc ()
        s = calc.add (a, b)

        self.assertEqual (s, c)

    def testAdd2(self):
        a = -6
        b = -5
        c = -11

        calc = Calc ()
        s = calc.add (a, b)

        self.assertEqual (s, c)

    def testAdd3(self):
        a = -6
        b = 5
        c = -1

        calc = Calc ()
        s = calc.add (a, b)

        self.assertEqual (s, c)

    def testAdd4(self):
        a = 6
        b = -5
        c = 1

        calc = Calc ()
        s = calc.add (a, b)

        self.assertEqual (s, c)

    def testAdd5(self):
        a = 6000000000000000000000000000000000000000000000000000000000000000
        b = 5
        c = 6000000000000000000000000000000000000000000000000000000000000005

        calc = Calc ()
        s = calc.add (a, b)

        self.assertEqual (s, c)
    def testMinus(self):
        a=6
        b=5
        c=1
        calc=Calc
        s=calc.minus(self,a, b)
        self.assertEqual(s,c)

    def testmulti(self):
            a = 6
            b = 5
            c = 30
            calc = Calc
            s = calc.multi (self,a, b)
            self.assertEqual (s, c)
    def testDevision(self):
        a=10
        b=5
        c=2
        calc=Calc
        s=calc.devision(self,a,b)
        self.assertEqual(s,c)