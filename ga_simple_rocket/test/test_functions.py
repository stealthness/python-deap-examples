"""
Extends unittest adding assert methods for Individual and Rocket
"""
import unittest

from ga_simple_rocket.config import *
from ga_simple_rocket.individual_class import Individual


class MyTest(unittest.TestCase):

    def assert_rocket(self, test_item, **kwargs):
        """

        :param rocket:
        :param kwargs:
        :return:
        """
        if type(test_item) is Individual:
            if 'fitness' in kwargs:
                self.assertAlmostEqual(kwargs['fitness'], test_item.fitness, TOL)
            rocket = test_item.rocket
        else:
            rocket = test_item
        if 'exp_name' in kwargs:
            self.assertEqual(kwargs['exp_name'], rocket.name, 'name')
        if 'exp_pos' in kwargs:
            self.assertEqual(kwargs['exp_pos'], rocket.pos, 'pos')
        if 'exp_vel' in kwargs:
            self.assertEqual(kwargs['exp_vel'], rocket.vel, 'vel')
        if 'exp_acc' in kwargs:
            self.assertEqual(kwargs['exp_acc'], rocket.acc, 'acc')
        if 'has_failed' in kwargs:
            self.assertEqual(kwargs['has_failed'], rocket.has_failed)
        if 'has_landed' in kwargs:
            self.assertEqual(kwargs['has_landed'], rocket.has_landed)

    def assert_individual(self, individual, **kwargs):
        self.assert_rocket(individual, **kwargs)


if __name__ == '__main__':
    unittest.main()