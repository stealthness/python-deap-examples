"""
Testing the Rocket class misc functions
"""
import numpy as np
from ga_rocket_example.rocket_class import Rocket
from ga_rocket_example.test.config import *
from ga_rocket_example.test.test_functions import MyTest  # extends unittest

TOL = 0.0001


class MyTestCase(MyTest):

    def setUp(self):
        self.r = Rocket('test')

    def test_set_pos(self):
        self.r.set(pos=ZERO)
        self.assertRocket(self.r, exp_pos=ZERO)
        
    def test_set_vel(self):
        self.r.set(vel=ZERO)
        self.assertRocket(self.r, exp_vel=ZERO)
        
    def test_set_acc(self):
        self.r.set(acc=ZERO)
        self.assertRocket(self.r, exp_acc=ZERO)

    def test_set_dir(self):
        self.r.set(dir=180)
        self.assertRocket(self.r, exp_dir=180)

    def test_set_dir_over_360(self):
        self.r.set(dir=361)
        self.assertRocket(self.r, exp_dir=1)

    def test_set_dir_under_0(self):
        self.r.set(dir=-90)
        self.assertRocket(self.r, exp_dir=270)
