"""
Testing a rocket class after 1 time interval
"""
import unittest
import numpy as np

from ga_rocket_example.config import TIME_INTERVALS
from ga_rocket_example.rocket_class import Rocket
from ga_rocket_example.test.config import *


def assert_rocket(rocket, **kwargs):
    """  
    :param rocket: 
    :param kwargs: 
                exp_pos
                exp_vel
                exp_acc
                exp_dir
    :return: 
    """
    if 'exp_pos' in kwargs:
        np.testing.assert_almost_equal(kwargs['exp_pos'], rocket.pos)
    if 'exp_vel' in kwargs:
        np.testing.assert_almost_equal(kwargs['exp_vel'], rocket.vel)
    if 'exp_acc' in kwargs:
        np.testing.assert_almost_equal(kwargs['exp_acc'], rocket.acc)
    if 'exp_dir' in kwargs:
        np.testing.assert_almost_equal(kwargs['exp_dir'], rocket.dir)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.rocket = Rocket('test')

    def test_init_rocket_at_rest(self):
        self.rocket.acc = ZERO
        assert_rocket(self.rocket, exp_pos=START_POS, exp_vel=ZERO, exp_acc=ZERO)

    def test_init_rocket_at_rest_with_gravity(self):
        assert_rocket(self.rocket, exp_pos=START_POS, exp_vel=ZERO, exp_acc=GRAVITY)

    def test_rocket_moving_at_rest_after_1_time_interval(self):
        self.rocket.acc = ZERO
        self.rocket.main_engine_on = True
        self.rocket.main_engine_max_force = 9.8  # counter act gravity
        assert_rocket(self.rocket, exp_pos=START_POS, exp_vel=ZERO, exp_acc=ZERO)
        dx, dy, dr = self.rocket.update([0, 1, 0])
        assert_rocket(self.rocket, exp_pos=START_POS, exp_vel=ZERO, exp_acc=ZERO)

    def test_rocket_moving_at_vel_after_1_time_interval(self):
        u = np.array([0.2, 10])
        self.rocket.acc = ZERO
        self.rocket.main_engine_on = True
        self.rocket.main_engine_max_force = 13.86 # counter act gravity
        self.dir = 45
        self.rocket.acc = ZERO
        self.rocket.vel = u
        assert_rocket(self.rocket, exp_pos=START_POS, exp_vel=u, exp_acc=ZERO)
        dx, dy, dr = self.rocket.update([0, 1, 0])
        assert_rocket(self.rocket, exp_pos=START_POS, exp_vel=u, exp_acc=ZERO)

    def test_rocket_moving_at_rest_with_gravity_after_1_time_interval(self):
        assert_rocket(self.rocket, exp_pos=START_POS, exp_vel=ZERO, exp_acc=GRAVITY)
        dx, dy, dr = self.rocket.update([0, 0, 0])
        assert_rocket(self.rocket, exp_pos=START_POS + np.array([dx, dy]), exp_vel=ZERO + GRAVITY / TIME_INTERVALS, exp_acc=GRAVITY)


