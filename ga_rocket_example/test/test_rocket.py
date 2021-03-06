"""
Testing the Rocket class
"""
import unittest
import numpy as np
from ga_rocket_example.rocket_class import Rocket
from ga_rocket_example.test.config import *
from ga_rocket_example.test.test_functions import MyTest  # extends unittest



class MyTestCase(MyTest):

    def setUp(self):
        self.r = Rocket('test')

    def test_init_rocket_at_rest(self):
        rocket = Rocket('Test')
        self.assertRocket(rocket, exp_pos=np.array([0.0, 10.0]), exp_vel=ZERO, exp_acc=GRAVITY, exp_dir=0)

    def test_init_rocket_at_100_with_initial_velocity(self):
        rocket = Rocket('Test')
        self.assertRocket(rocket, exp_pos=np.array([0.0, 10.0]), exp_vel=ZERO, exp_acc=GRAVITY, exp_dir=0)

    def test_rocket_in_equilibrium(self):
        rocket = Rocket('Test')
        rocket.main_engine_on = True
        rocket.main_engine_max_force = 9.8
        for i in range(10):
            rocket.update([0, 1, 0])
            self.assertRocket(rocket, exp_pos=np.array([0.0, 10.0]), exp_vel=ZERO, exp_acc=ZERO, err_msg=f'i:{i}, ')

        self.assertRocket(rocket, exp_pos=np.array([0.0, 10.0]),  exp_vel=ZERO, exp_acc=ZERO, exp_dir=0,
                          err_msg=f'final:, ')

    def test_ds_change_in_dr(self):
        self.assertRocket(self.r, exp_dr=0, exp_pos=START_POS, err_msg='test')

    def test_ds_change_in_dr_to_10(self):
        self.assertRocket(self.r, exp_dr=10, exp_pos=START_POS, err_msg='test')


if __name__ == '__main__':
    unittest.main()
