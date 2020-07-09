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
        self.test_test_individual_setup()
        self.individual.set(pos=0.0, vel=0.0)
        self.individual.calculate_fitness(0, 100)
        exp_fitness = 0.0
        err_msg = f'exp:{exp_fitness}, act:{self.individual.fitness}'
        self.assertIndividual(self.individual, has_landed=True, has_failed=False, msg=f'{self.individual}')
        self.assertAlmostEqual(exp_fitness, self.individual.fitness, delta=MyTest.TOL, msg=err_msg)

    def test_fail_crash(self):
        self.test_test_individual_setup()
        self.individual.set(pos=-10.0, vel=-10.0)
        self.individual.update(1)
        self.individual.calculate_fitness(10, 100)
        exp_fitness = 1.0
        err_msg = f'exp:{exp_fitness}, act:{self.individual.fitness}'
        self.assertIndividual(self.individual, has_landed=False, has_failed=True)
        self.assertAlmostEqual(exp_fitness, self.individual.fitness, delta=MyTest.TOL, msg=err_msg)

    def test_fail_too_high(self):

        self.individual.set(pos=550.0, vel=10)
        self.individual.rocket.update()
        self.individual.calculate_fitness(10, 100)
        exp_fitness = 1.0
        err_msg = f'exp:{exp_fitness}, act:{self.individual.fitness}'
        self.assertAlmostEqual(exp_fitness, self.individual.fitness, delta=MyTest.TOL, msg=err_msg)
        self.assertIndividual(self.individual, has_landed=False, has_failed=True)

    def test_not_landed_in_50(self):
        self.individual.calculate_fitness(50, 100)
        exp_fitness = 0.5
        err_msg = f'exp:{exp_fitness}, act:{self.individual.fitness}'
        self.assertIndividual(self.individual, has_landed=True, has_failed=False, msg=f'{self.individual}')
        self.assertAlmostEqual(exp_fitness, self.individual.fitness, delta=MyTest.TOL, msg=err_msg)

    def test_landed_in_50(self):
        self.individual.calculate_fitness(20, 100)
        exp_fitness = 0.8
        err_msg = f'exp:{exp_fitness}, act:{self.individual.fitness}'
        self.assertIndividual(self.individual, has_landed=True, has_failed=False, msg=f'{self.individual}')
        self.assertAlmostEqual(exp_fitness, self.individual.fitness, delta=MyTest.TOL, msg=err_msg)

    def test_landed_in_50(self):
        self.individual.calculate_fitness(90, 100)
        exp_fitness = 0.1
        err_msg = f'exp:{exp_fitness}, act:{self.individual.fitness}'
        self.assertIndividual(self.individual, has_landed=True, has_failed=False, msg=f'{self.individual}')
        self.assertAlmostEqual(exp_fitness, self.individual.fitness, delta=MyTest.TOL, msg=err_msg)

    def test_test_individual_setup(self):
        print(f'test_individual: {self.individual}')
        self.assertIndividual(self.individual, has_landed=False, has_failed=False, msg=f'{self.individual}')

