"""
The purpose of this file is to demonstrate the most simple use case of genetic algorithm using DEAP by solving the
one max problem
"""
from deap import base, creator, tools

import random
import matplotlib.pyplot as plt

# problem constants

ONE_MAX_LENGTH = 100    # length of the bitstring to be optimised

# Genetic Algorithm Constants
POP_SIZE = 200              # size of the population
PROB_CROSSOVER = 0.9        # probability for crossover an individual
PROB_MUTATION = 0.1         # probability of mutation an individual
MAX_GENERATIONS = 50        # the maximum number generation stooping criteria

RANDOM_SEED = 42
random.seed(RANDOM_SEED)    # set the random seed to have reproducible results

# start by creating a toolbox and register function to create random digits of 0 or 1

toolbox = base.Toolbox()
toolbox.register("zeroOrOne", random.randint, 0, 1)

# create a fitness class which will be suing fitnessMAx strategy

creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# create the individual class to represent a single string of zero and ones, adding attribute fitness with our selected
# FitnessMAx function in toolbox

creator.create("Individual", list, fitness=creator.FitnessMax)

# create an operator function to create individuals

toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.zeroOrOne, ONE_MAX_LENGTH)
# create the popluation, using the individualCreator that we just declared

toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


def oneMaxFitness(individual):
    """
    Find the fitness value of the individual, which is the sum of the digits. lowest fitness will be all zeros, highest
    fitness values will be all ones
    :param individual:
    :return: a tuple that is single value sum of the digits
    """
    return sum(individual),     # return a tuple


# Now we will define evaluate function using the above fitness function

toolbox.register("evaluate", oneMaxFitness)

# using genetic operators in tools modules by aliasing with these existing functions

toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/ONE_MAX_LENGTH)

# now we can start creating the intial population

population = toolbox.populationCreator(n=POP_SIZE)

print(population)