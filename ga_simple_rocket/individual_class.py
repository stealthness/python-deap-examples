"""
This file holds the class Individual
"""
from random import random

from ga_simple_rocket.config import *
from ga_simple_rocket.simple_rocket_class import SimpleRocket


def fitness_function_simple(rocket, t, max_t) -> float:
    """
    Calculates the the fitness of the rocket position from the target location
        if rocket has failed:
            then fitness is 1.0
        if rocket has succeeded:
            then fitness will be 0.0 + relative time taken
            relative time will be  1.0 - t / max_time
    :param: time
    :param: max time allowed
    :return: fitness of the individual
    """
    if rocket.has_failed:
        fitness = 1.0
    elif rocket.has_landed:
        if t == 0:
            fitness = 0.0
        else:
            fitness = 1.0 - t / max_t
    else:
        fitness = 1.0 - t / max_t
    return fitness


class Individual:
    """
    the class individual holds a
    -- rocket object
    -- target location
    -- commands (individuals chromosomes)
    """

    def __init__(self, name, **kwargs):
        self.rocket = SimpleRocket(name, **kwargs)
        self.fitness: float = 1.0
        self.fitness_function = fitness_function_simple
        self.target: float = GROUND_LEVEL
        self.commands = []
        self.generate_commands()
        self.max_time = MAX_TIME_INTERVALS

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > len([self.commands]):
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
        Updates the the Individuals rocket for command[t]. Returns the displacement and fitness\n
        :param t: current time interval
        :return: ds, fitness
        """
        if self.rocket.has_failed:
            ds = 0.0
        elif self.rocket.has_landed:
            ds = 0.0
        else:
            if self.commands[t] == 1:
                self.rocket.engine_on = True
            else:
                self.rocket.engine_on = False
            ds = self.rocket.update()
        self.has_failed()
        self.has_landed()
        self.calculate_fitness(t, self.max_time)
        return ds, self.fitness

    def calculate_fitness(self, t: int, max_t=MAX_TIME_INTERVALS) -> float:
        self.fitness = self.fitness_function(self.rocket, t, max_t)
        return self.fitness

    def has_failed(self) -> bool:
        """
        checks if the individual rocket has fails, and then
        :return:
        """
        if self.rocket.pos >= MAX_ROCKET_HEIGHT:  # check rocket height
            self.rocket.self_destruct()
            return True
        elif GROUND_LEVEL - TOL > self.rocket.pos:  # check ground level
            self.rocket.self_destruct()
            return True
        elif GROUND_LEVEL - TOL < self.rocket.pos <= GROUND_LEVEL + TOL and -TOL < self.rocket.vel < TOL:
            self.rocket.complete_landing()
            return False
        else:
            return False

    def has_landed(self) -> bool:
        HEIGHT_TOL = 10
        if self.rocket.pos < GROUND_LEVEL + HEIGHT_TOL and -HEIGHT_TOL < self.rocket.vel < HEIGHT_TOL:
            self.rocket.has_landed = True
            return True

    def generate_commands(self):
        for x in range(MAX_TIME_INTERVALS):
            if random() < GENERATE_ENGINE_PROB_FIRE and GENERATE_RANDOM_COMMANDS:
                self.commands.append(1)
            else:
                self.commands.append(0)#

    def set(self, **kwargs):
        if 'name' in kwargs:
            self.rocket.name = kwargs['name']
        if 'pos' in kwargs:
            self.rocket.pos = kwargs['pos']
        if 'vel' in kwargs:
            self.rocket.vel = kwargs['vel']
        if 'acc' in kwargs:
            self.rocket.acc = kwargs['acc']





