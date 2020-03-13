import unittest

from ga_simple_rocket.config import *
from ga_simple_rocket.individual_class import Individual

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.individual = Individual('r0')
        self.individual.target = 0.0

    def test_create_individual(self):
        self.assert_individual(self.individual, exp_name='r0', has_failed=False)

    def test_rocket_crashed_below_ground(self):
        self.individual.rocket.pos = GROUND_LEVEL - 10.0
        self.assert_individual(self.individual, fitness=1.0, has_failed=False)

    def test_rocket_gone_high(self):
        self.individual.rocket.pos = MAX_ROCKET_HEIGHT + 1.0
        self.individual.calculate_fitness()
        self.assert_individual(self.individual, fitness=1.0, has_failed=True)

    def test_rocket_has_landed(self):
        self.individual.rocket.pos = -0.0000034
        self.individual.rocket.vel = -0.0000076
        self.individual.rocket.acc = 0.00045
        self.individual.calculate_fitness()
        self.assert_individual(self.individual, fitness=1.0, has_landed=True, has_failed=False)

    def test_rocket_reaches_max_height(self):
        t = 0
        self.individual.commands = [1]*100
        self.individual.rocket.engine_force = 40
        while t < 100:
            self.individual.update(t)
            t += 1
        self.assert_individual(self.individual, fitness=1.0, has_failed=True)
        self.assertTrue(MAX_ROCKET_HEIGHT + self.individual.rocket.vel + 10 > self.individual.rocket.pos, 'rocket still moing')

    def test_rocket_free_falls_and_crashes(self):
        t = 0
        self.individual.commands = [0]*100
        self.individual.rocket.engine_force = 40
        self.individual.rocket.pos = 100
        while t < 100:
            self.individual.update(t)
            t += 1
        self.assert_individual(self.individual, has_failed=True)

    def assert_rocket(self, rocket, **kwargs):
        if type(rocket) is Individual:
            if 'fitness' in kwargs:
                self.assertAlmostEqual(kwargs['fitness'], rocket.fitness, TOL)
            rocket = rocket.rocket
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
