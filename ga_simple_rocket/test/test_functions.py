"""
Extends unittest adding assert methods for Individual and Rocket
"""
import unittest

from ga_simple_rocket.config import *
from ga_simple_rocket.individual_class import Individual


class MyTest(unittest.TestCase):

    TOL: float = 0.0001

    def assertTestItem(self, test_item, **kwargs):
        """
        Assert Test for Individual and Rockets classes \n
        :param test_item: Individual or Rocket class
        :param kwargs:
            'exp_name'
            'exp_pos'
        :return: None
        """
        if type(test_item) is Individual:
            if 'fitness' in kwargs:
                self.assertAlmostEqual(kwargs['fitness'], test_item.fitness,
                                       delta=TOL, msg=f'exp:{kwargs["fitness"]}, act:{kwargs["fitness"]}')
            rocket = test_item.rocket
        else:
            rocket = test_item
        if 'exp_name' in kwargs:
            self.assertEqual(kwargs['exp_name'], rocket.name, msg=f'exp:{kwargs["exp_name"]}, act:{rocket.name}')
        if 'exp_pos' in kwargs:
            self.assertAlmostEqual(kwargs['exp_pos'], rocket.pos,
                                   delta=TOL, msg=f'exp:{kwargs["exp_pos"]}, act:{rocket.pos}')
        if 'exp_vel' in kwargs:
            self.assertAlmostEqual(kwargs['exp_vel'], rocket.vel,
                                   delta=TOL, msg=f'exp:{kwargs["exp_pos"]}, act:{rocket.pos}')
        if 'exp_acc' in kwargs:
            self.assertAlmostEqual(kwargs['exp_acc'], rocket.acc, 'acc',
                                    delta=TOL, msg=f'exp:{kwargs["exp_acc"]}, act:{rocket.pos}')
        if 'has_failed' in kwargs:
            self.assertEqual(kwargs['has_failed'], rocket.has_failed,
                             msg=f'has_failed -> exp:{kwargs["has_failed"]}, act:{rocket.has_failed}')
        if 'has_landed' in kwargs:
            self.assertEqual(kwargs['has_landed'], rocket.has_landed,
                             msg=f'has_landed -> exp:{kwargs["has_landed"]}, act:{rocket.has_landed}')
        if 'exp_target' in kwargs:
            self.assertEqual(kwargs['exp_target'], rocket.target,
                             msg=f'target -> exp:{kwargs["has_landed"]}, act:{rocket.has_landed}')

    def assertRocket(self, rocket, **kwargs):
        """
        Assert Test for Individual and Rockets classes\n
        :param rocket: Individual or Rocket class
        :param kwargs:
            'exp_name'
            'exp_pos'
        :return: None
        """
        self.assertTestItem(rocket, **kwargs)

    def assertIndividual(self, individual, **kwargs):
        """
        Assert Test for Individual and Rockets classes\n
        :param individual: Individual class
        :param kwargs:
            'exp_name'
            'exp_pos'
        :return: None
        """
        self.assertTestItem(individual, **kwargs)

    def set_rocket(self, test_item, **kwargs):
        """
        :param test_item:
        :param kwargs:
        :return:
        """
        if type(test_item) is Individual:
            rocket = test_item.rocket
        else:
            rocket = test_item
        if 'pos' in kwargs:
            rocket.pos = kwargs['pos']
        if 'vel' in kwargs:
            rocket.pos = kwargs['vel']
        if 'acc' in kwargs:
            rocket.pos = kwargs['acc']
        if 'has_landed' in kwargs:
            rocket.pos = kwargs['has_landed']
        if 'has_failed' in kwargs:
            rocket.pos = kwargs['has_failed']

    def set_individual(self, individual, **kwargs):
        self.set_rocket(individual, **kwargs)


if __name__ == '__main__':
    unittest.main()