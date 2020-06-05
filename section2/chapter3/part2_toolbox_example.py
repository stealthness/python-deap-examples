"""
Purpose of this script is to demonstrate the use of the toolbox module
"""
from random import random

from deap import base
from deap import tools

# we going to show how we can create new operators by customizing other functions
print('start')

def sumOfTwo(a, b):
    return a + b


toolbox = base.Toolbox()
toolbox.register('incrementByFive', sumOfTwo, b=5)

print(f'increment 10 by five is : {toolbox.incrementByFive(10)}')

# Since many genetic operators are use often, the tools module contain numerous functions that can be used to create
# useful functions

toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.02)

# Create the population using initRepeat function in tools

randomList = tools.initRepeat(list, random.random, 30)

# we can also use a function to create a list


def zeroOrOneV1():
    return random.randint(0, 1)

randomList = tools.initRepeat(list, zeroOrOneV1(), 30)

# or we could take advantage of the toolbox

toolbox.register("zeroOrOneV2", random.randint, 0, 1)
randomList = tools.initRepeat(list, toolbox.zeroOrOneV2, 30)

# finally we can also create our own fitness function to evaluate


def someFitnessCalculationFunction(individual):
    # return _some_calculation_of_the_fitness
    return random.random(0, 1)


toolbox.register("evaluate",someFitnessCalculationFunction)

print('end')
