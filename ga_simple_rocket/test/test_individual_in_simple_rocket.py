import unittest

from ga_simple_rocket.config import *
from ga_simple_rocket.individual_class import Individual


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.individual = Individual('r0')
        self.individual.target = 0.0

    def test_create_individual(self):
        self.assertFalse(self.individual.rocket.has_failed)
        self.assertEqual('r0', self.individual.rocket.name)

    def test_rocket_crashed_below_ground(self):
        self.individual.rocket.pos = GROUND_LEVEL - 10.0
        self.assertEqual(1, self.individual.calculate_fitness())
        self.assertTrue(self.individual.rocket.has_failed)

    def test_rocket_gone_high(self):
        self.individual.rocket.pos = MAX_ROCKET_HEIGHT + 1.0
        self.assertEqual(1, self.individual.calculate_fitness())
        self.assertTrue(self.individual.rocket.has_failed, f'{self.individual}')

    def test_rocket_has_landed(self):
        self.individual.rocket.pos = -0.0000034
        self.individual.rocket.vel = -0.0000076
        self.individual.rocket.acc = 0.00045
        self.assertTrue(self.individual.has_landed())

    def test_rocket_reaches_max_height(self):
        t = 0
        self.individual.commands = [1]*100
        self.individual.rocket.engine_force = 40
        while t < 100:
            self.individual.update(t)
            t += 1
        self.assertTrue(self.individual.has_failed(), f'Not reached max level {self.individual.rocket.pos}')
        self.assertTrue(MAX_ROCKET_HEIGHT + self.individual.rocket.vel + 10 > self.individual.rocket.pos, 'rocket still moing')

    def test_rocket_freefalls_and_crashes(self):
        t = 0
        self.individual.commands = [0]*100
        self.individual.rocket.engine_force = 40
        while t < 100:
            self.individual.update(t)
            t += 1
        self.assertTrue(self.individual.has_failed(), f'has crashed {self.individual.rocket.pos}')




if __name__ == '__main__':
    unittest.main()
