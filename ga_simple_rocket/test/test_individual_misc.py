import unittest

from ga_simple_rocket.individual_class import Individual
from ga_simple_rocket.test.test_functions import MyTest


class MyTestCase(MyTest):

    def setUp(self):
        self.individual = Individual('test')
        self.individual.set(pos=100.0)
        self.individual.set(max_tim=90)
        self.assert_individual(self.individual, exp_pos=100.0, max_time=90)



if __name__ == '__main__':
    unittest.main()
