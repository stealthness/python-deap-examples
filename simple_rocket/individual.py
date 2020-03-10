"""
This file holds the class Individual
"""
from random import random

from ga_rocket_example import config
from ga_simple_rocket.config import GENERATE_ENGINE_PROB_FIRE, MAX_TIME_INTERVALS
from simple_rocket.rocket import SimpleRocket


class Individual:
    """
    the class individual holds a
    -- rocket object
    -- target location
    -- commands (individuals chromosomes)
    """

    def __init__(self, name):
        self.rocket = SimpleRocket(name)
        self.fitness: float = 1.0
        self.target: float = config.GROUND_LEVEL
        self.commands = []
        self.generate_commands()

    def __str__(self):
        return f'name: {self.rocket.name}, fitness:{self.fitness}, rocket:{self.rocket}'

    def update(self, t):
        print(f't:{t}')
        if self.commands[t] == 1:
            self.rocket.engine_on = True
        else:
            self.rocket.engine_on = False
        delta_s = self.rocket.update()
        fitness = self.calculate_fitness
        return delta_s, fitness


    def calculate_fitness(self) -> float:
        """
        Calculates the the fitness of the rocket position from the target location
        :return: fitness of the individual
        """
        if self._has_failed():
            return 1.0
        if self.rocket.pos - self.target < 1e-10:
            return 1.0
        else:
            return 1 / (1 + 1/(self.rocket.pos - self.target))

    def _has_failed(self):
        TOL = 0.1
        if config.MAX_ROCKET_HEIGHT < self.rocket.pos:
            # too high
            self.rocket.exploded()
            return True
        elif config.GROUND_LEVEL + TOL < self.rocket.pos:
            return False
        elif config.GROUND_LEVEL - TOL < self.rocket.pos <= config.GROUND_LEVEL + TOL and -TOL < self.rocket.vel < TOL and -TOL < self.rocket.acc < TOL:
            self.rocket.complete_landing()
            return False
        else:
            self.rocket.exploded()
            return True

    def has_landed(self) -> bool:
        TOL = 0.1
        if self.rocket.pos < config.GROUND_LEVEL and -TOL < self.rocket.vel < TOL and -TOL < self.rocket.acc < TOL:
            self.rocket.has_landed = True
            return True

    def generate_commands(self):
        new_commands = []
        for x in range(MAX_TIME_INTERVALS):
            if random() < GENERATE_ENGINE_PROB_FIRE:
                self.commands.append(1)
            else:
                self.commands.append(0)




