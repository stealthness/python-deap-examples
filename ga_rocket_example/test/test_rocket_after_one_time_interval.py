"""
Testing a rocket class after 1 time interval
"""
import unittest
import numpy as np

from ga_rocket_example.rocket_class import Rocket

zero = np.array([0.0, 0.0])
start_pos = np.array([0.0, 10.0])

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.rocket = Rocket('test')

    def test_init_rocket_at_rest(self):
        np.testing.assert_almost_equal(start_pos, self.rocket.pos)
