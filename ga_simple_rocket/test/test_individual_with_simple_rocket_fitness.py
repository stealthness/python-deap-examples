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
        self.individual.set(pos=0.0, vel=0.0)
        self.individual.calculate_fitness(0, 100)
        exp_fitness = 0.0

        self.assert_individual(self.individual, has_landed=True, has_failed=False)
        self.assertAlmostEqual(exp_fitness, self.individual.fitness, delta=MyTest.TOL,
                               msg=f'exp:{exp_fitness}, act:{self.individual.fitness}')

        self.assertEqual('test', self.individual.rocket.name)

    def test_fail_crash(self):
        self.assert_individual(self.individual, exp_name='test')
        self.individual.set(pos=-10.0, vel=-10.0)
        self.individual.calculate_fitness(10, 100)
        exp_fitness = 1.0

        self.assertAlmostEqual(exp_fitness, self.individual.fitness, delta=MyTest.TOL)

        self.assert_individual(self.individual, has_landed=False, has_failed=True)
        self.assertEqual('test', self.individual.rocket.name)

