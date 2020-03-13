"""
Purpose of this file is to test the fitness methodology of a simple rocket
The fitness measure
"""
from ga_simple_rocket.individual_class import Individual
from ga_simple_rocket.test.test_functions import MyTest
# MyTest is extension of unittest


class TestIndividualFitness(MyTest):

    def setUp(self):
        self.individual = Individual('test')

    def test_success_t_0(self):
        self.assert_individual(self.individual, exp_name='test')
        self.assertEqual('test', self.individual.rocket.name)


