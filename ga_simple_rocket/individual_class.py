"""
This file holds the class Individual
"""
import math
from random import random
import numpy as np

from ga_rocket_example import config
from ga_simple_rocket.config import GENERATE_ENGINE_PROB_FIRE, MAX_TIME_INTERVALS, TOL, MAX_ROCKET_HEIGHT
from ga_simple_rocket.simple_rocket_class import SimpleRocket


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
        return f'name: {self.rocket.name}, fitness:{self.fitness:.3f}, rocket:{self.rocket}'

    def update(self, t):
        """
        Updates the the Individuals rocket for command[t]. Returns the displacement and fitness
        :param t:
        :return:
        """
        if self.commands[t] == 1:
            self.rocket.engine_on = True
        else:
            self.rocket.engine_on = False
        ds = self.rocket.update()
        fitness = self.calculate_fitness
        return ds, fitness

    def calculate_fitness(self) -> float:
        """
        Calculates the the fitness of the rocket position from the target location
        :return: fitness of the individual
        """
        if self.has_failed():
            return 1.0
        if self.rocket.pos - self.target < 1e-10:
            return 1.0
        else:
            return 1 / (1 + 1/np.abs(self.rocket.pos - self.target))

    def has_failed(self) -> bool:
        """
        checks if the individual rocket has fails, and then
        :return:
        """
        if self.rocket.pos >= MAX_ROCKET_HEIGHT:  # check rocket height
            self.rocket.self_destruct()
            return True
        elif config.GROUND_LEVEL - TOL > self.rocket.pos:  # check ground level
            self.rocket.self_destruct()
            return True
        elif config.GROUND_LEVEL - TOL < self.rocket.pos <= config.GROUND_LEVEL + TOL and -TOL < self.rocket.vel < TOL:
            self.rocket.complete_landing()
            return False
        else:
            return False

    def has_landed(self) -> bool:
        TOL = 10
        if self.rocket.pos < config.GROUND_LEVEL + TOL and -TOL < self.rocket.vel < TOL :
            self.rocket.has_landed = True
            return True

    def generate_commands(self):
        new_commands = []
        for x in range(MAX_TIME_INTERVALS):
            if random() < GENERATE_ENGINE_PROB_FIRE:
                self.commands.append(1)
            else:
                self.commands.append(0)




