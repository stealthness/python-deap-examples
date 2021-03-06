from ga_simple_rocket.config import *
from ga_simple_rocket.individual_class import Individual
from ga_simple_rocket.test.test_functions import MyTest


class TestIndividualSimpleRocket(MyTest):

    def setUp(self):
        self.individual = Individual('r0')
        self.individual.target = 0.0

    def test_create_individual(self):
        self.assertIndividual(self.individual, exp_name='r0', has_failed=False)

    def test_rocket_crashed_below_ground(self):
        self.individual.rocket.pos = GROUND_LEVEL - 10.0
        self.assertIndividual(self.individual, fitness=1.0, has_failed=False)

    def test_rocket_gone_high(self):
        self.individual.rocket.pos = MAX_ROCKET_HEIGHT + 1.0
        self.individual.has_failed()
        self.individual.calculate_fitness(0, 100)
        print(self.individual)
        self.assertIndividual(self.individual, fitness=1.0, has_failed=True)

    def test_rocket_has_landed(self):
        self.individual.rocket.pos = -0.0000034
        self.individual.rocket.vel = -0.0000076
        self.individual.rocket.acc = 0.00045
        self.individual.has_landed()
        self.individual.calculate_fitness(0, 100)
        self.assertIndividual(self.individual, fitness=1.0, has_landed=True, has_failed=False)

    def test_rocket_reaches_max_height(self):
        t = 0
        self.individual.commands = [1]*100
        self.individual.rocket.engine_force = 40
        self.individual.rocket.pos = 10

        self.individual.update(t)
        t += 1
        while t < 100:
            self.individual.update(t)
            t += 1
        print(self.individual)
        self.assertTrue(MAX_ROCKET_HEIGHT < self.individual.rocket.pos, 'rocket still moving')
        self.assertIndividual(self.individual, fitness=1.0, has_failed=True)


if __name__ == '__main__':
    MyTest.main()
