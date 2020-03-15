"""
Testing the Rocket class
"""
import unittest
import numpy as np
from ga_rocket_example.rocket_class import Rocket
from ga_rocket_example.test.test_functions import MyTest  # extends unittest

TOL = 0.0001

ZERO = np.array([0.0, 0.0])
GRAVITY = np.array([0.0, -9.8])

class MyTestCase(MyTest):

    def test_init_rocket_at_rest(self):
        rocket = Rocket('Test')
        self.assertRocket(rocket, exp_pos=np.array([0.0, 10.0]), exp_vel=ZERO, exp_acc=GRAVITY)

    def test_init_rocket_at_100_with_initial_velocity(self):
        rocket = Rocket('Test')
        self.assertRocket(rocket, exp_pos=np.array([0.0, 10.0]), exp_vel=ZERO, exp_acc=GRAVITY)

    def test_rocket_in_equilibrium(self):
        rocket = Rocket('Test')
        rocket.main_engine_on = True
        rocket.main_engine_max_force = 9.8
        for i in range(10):
            rocket.update([0, 1, 0])
            self.assertRocket(rocket, exp_pos=np.array([0.0, 10.0]), exp_vel=ZERO, exp_acc=ZERO, err_msg=f'i:{i}, ')

        self.assertRocket(rocket, exp_pos=np.array([0.0, 10.0]),  exp_vel=ZERO, exp_acc=ZERO,
                          err_msg=f'final:, ')


if __name__ == '__main__':
    unittest.main()
