import unittest

from ga_simple_rocket.individual_class import Individual
from ga_simple_rocket.test.test_functions import MyTest


class MyTestCase(MyTest):

    def setUp(self):
        self.individual = Individual('test')
        self.individual.set(pos=100.0)
        self.individual.set(max_tim=90)
        self.assertIndividual(self.individual, exp_pos=100.0, max_time=90)

    def test_create(self):
        self.assertIndividual(self.individual, pos=100.0)

    def test_overwrite_with_new_individual(self):
        self.individual = Individual('test', pos=50.0)
        self.assertIndividual(self.individual, pos=50.0)

    def test_change_pos(self):
        self.individual.set(pos=50.0)
        self.assertIndividual(self.individual, pos=50.0)

    def test_change_v(self):
        self.individual.set(vel=50.0)
        self.assertIndividual(self.individual, vel=50.0)

    def test_change_acc(self):
        self.individual.set(acc=50.0)
        self.assertIndividual(self.individual, acc=50.0)





if __name__ == '__main__':
    unittest.main()
