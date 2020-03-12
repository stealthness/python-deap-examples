"""
Testing the Rocket class
"""
import unittest
import numpy as np
from ga_rocket_example.rocket_class import Rocket

TOL = 0.0001


class MyTestCase(unittest.TestCase):

    def test_init_rocket_at_rest(self):
        rocket = Rocket('Test')
        np.testing.assert_allclose(np.array([0.0, 40.0]), rocket.pos, err_msg="pos")
        np.testing.assert_allclose(np.array([0.0, 0.0]), rocket.vel, err_msg="vel")
        np.testing.assert_allclose(np.array([0.0, 0.0]), rocket.acc, err_msg="acc", rtol=TOL, atol=TOL)
        self.assertTrue(True)

    def test_rocket_in_equilibrium(self):
        rocket = Rocket('Test')
        rocket.main_engine_max_force = 9.8
        for i in range(10):
            rocket.update([0,1,0])

        np.testing.assert_allclose(np.array([0.0, 40.0]), rocket.pos, err_msg="pos")
        np.testing.assert_allclose(np.array([0.0, 0.0]), rocket.vel, err_msg="vel")
        np.testing.assert_allclose(np.array([0.0, 0.0]), rocket.acc, err_msg="acc", rtol=TOL, atol=TOL)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
