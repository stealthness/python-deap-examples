""":arg"""
from ge_rocket_example import config
from rocket.rocket import Rocket


class Population:
    """
    Population will hold a list of Rockets
    and a list of associated instruction on firing a its rockets
    """

    def __init__(self, population_size):
        self.population_size = population_size
        self.rockets = []
        self.rockets_fitness = []
        for r in range(population_size):
            self.rockets.append(Rocket(f'rocket{r}', [[0, 1, 1]] * 30 + [[0, 0, 0]] * 92))

    def get_rocket(self, index):
        if self.population_size < index < 0:
            raise IndexError()
        return self.rockets[index]

    def get_fitness(self):
        for rocket in self.rockets:
            self.rockets_fitness = rocket.check_distance_from(config.TARGET_POSITION)
        return self.rockets_fitness

    def has_finished(self):
        """
        Checks to see if population of rockets has any active rockets left
        :return:
        """
        for rocket in self.rockets:
            if rocket.has_reached_target(config.TARGET_POSITION):
                print(f'Has finished is TRUE')
                return True
            if not rocket.has_exploded:
                print(f'Has finished is False')
                return False
        return True
