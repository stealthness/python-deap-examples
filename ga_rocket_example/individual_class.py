"""
This file holds the class Individual
"""
from random import random
import numpy as np

from ga_rocket_example import config
from ga_rocket_example.rocket_class import Rocket, MAX_ROCKET_HEIGHT


class Individual:
    """
    the class individual holds a
    -- rocket object
    -- target location
    -- commands (individuals chromosomes)
    """

    def __init__(self, name):
        self.rocket = Rocket(name)
        self.fitness: float = 1.0
        self.target: np.array = config.TARGET_POSITION
        self.commands = []
        self.generate_commands()

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > len[self.commands]:
            raise StopIteration
        self.n += 1
        return self.commands[self.n]

    def __str__(self):
        return f'name: {self.rocket.name}, fitness:{self.fitness:.3f}, rocket:{self.rocket}'

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __len__(self):
        return len(self.commands)

    def update(self, t):
        """
        Updates the the Individuals rocket for command[t]. Returns the displacement and fitness
        :param t:
        :return:
        """
        if self.rocket.has_failed:
            ds = np.array([0, 0])
            fitness = 1.0
        elif self.rocket.has_landed:
            ds = np.array([0, 0])
            fitness = 0.0
        else:
            if self.commands[t][1] == 1:
                self.rocket.main_engine_on = True
            elif self.commands[t][0] == 1:
                self.rocket.dir += 3
            elif self.commands[t][2] == 1:
                self.rocket.dir -= 3
            else:
                self.rocket.main_engine_on = False
            ds = self.rocket.update()
            fitness = self.calculate_fitness()
        return ds, fitness

    def calculate_fitness(self) -> float:
        """
        Calculates the the fitness of the rocket position from the target location
        :return: fitness of the individual
        """
        if self.has_failed():
            return 1.0
        if self.rocket.pos - self.target < 1e-10:
            return 0.0
        else:
            return 1 / (1 + 1/np.linalg(self.rocket.pos, self.target))

    def has_failed(self) -> bool:
        """
        checks if the individual rocket has fails, and then
        :return:
        """
        TOL = 0.0
        if self.rocket.pos[1] >= MAX_ROCKET_HEIGHT:  # check rocket height
            self.rocket.self_destruct()
            return True
        elif config.GROUND_LEVEL - TOL > self.rocket.pos[1]:  # check ground level
            self.rocket.self_destruct()
            return True
        # elif config.GROUND_LEVEL - TOL < self.rocket.pos <= config.GROUND_LEVEL + TOL and -TOL < self.rocket.vel < TOL:
        #     self.rocket.complete_landing()
        #     return False
        else:
            return False

    def has_landed(self) -> bool:
        TOL = 10
        if np.linalg(self.rocket.pos, self.target) < 1e-10:
            self.rocket.has_landed = True
            return True

    def generate_commands(self):
        for x in range(MAX_TIME_INTERVALS):
            if random() < GENERATE_ENGINE_PROB_FIRE and GENERATE_RANDOM_COMMANDS:
                self.commands.append(1)
            else:
                self.commands.append(0)
