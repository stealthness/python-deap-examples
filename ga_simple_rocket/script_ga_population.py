"""
Purpose of this file is generate population and then
"""
import random

from deap import base
from deap import creator
from deap import tools

from ga_simple_rocket.config import MAX_TIME_INTERVALS
from ga_simple_rocket.individual_class import Individual
from ga_simple_rocket.functions import select_roulette, mutate_individual

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", Individual, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator
#                      define 'attr_bool' to be an attribute ('gene') which corresponds to integers sampled uniformly
#                      from the range [0,1] (i.e. 0 or 1 with equal probability)
toolbox.register("attr_bool", random.randint, 0, 1)

# Structure initializers
#                         define 'individual' to be an individual consisting of 100 'attr_bool' elements ('genes')
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, MAX_TIME_INTERVALS)

# define the population to be a list of individuals
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def eval_fitness(individual):
    # run the rocket commanda
    for t in range(MAX_TIME_INTERVALS):
        _, _ = individual.update(t)
    return individual.fitness,

# Create random seed
random.seed(1)

# create an initial population of 300 individuals (where
# each individual is a list of integers)
pop = toolbox.population(n=10)

# Operator registration :
#       register the goal / fitness function
toolbox.register("evaluate", eval_fitness)

#       register the crossover operator
toolbox.register("mate", tools.cxTwoPoint)

# register a mutation operator with a probability to
# flip each attribute/gene of 0.05
toolbox.register("mutate", mutate_individual, indpb=0.05)

# operator for selecting individuals for breeding the next
# generation: each individual of the current generation
# is replaced by the 'fittest' (best) of three individuals
# drawn randomly from the current generation.
toolbox.register("select", select_roulette)

# CXPB  is the probability with which two individuals are crossed
# MUTPB is the probability for mutating an individual
CXPB, MUTPB = 0.5, 0.2

# Evaluate the entire population
fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):

    ind.fitness = fit

# Extracting all the fitnesses of
fits = [ind.fitness[0] for ind in pop]

g = 0

while max(fits) > 0.0 and g < 100:
    # A new generation
    g = g + 1
    print(f"-- Generation {g} --")

    # Select the next generation individuals
    offspring = toolbox.select(pop, len(pop))

    for mutant in offspring:
        # mutate an individual with probability MUTPB
        if random.random() < MUTPB:
            toolbox.mutate(mutant)

    for x in range(5, 10):
        print('l')
