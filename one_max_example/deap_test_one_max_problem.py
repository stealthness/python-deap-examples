import random
from deap import creator, base, tools, algorithms
'''
The purpose of this file is the One Max Problem using DEAP genetic algoritm package
'''

W0 = 1.0
INDIVIDUAL_LENGTH = 50
MAX_GEN = 20
TERMINATE_ON_SOLUTION = True


def printTop(top):
    for item in top:
        print(item)


print("start")
creator.create("FitnessMax", base.Fitness, weights=(W0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=INDIVIDUAL_LENGTH)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evalOneMax(individual):
    """
    The evaluation of one max problem is the sum of the individual chromosomes, where 0 is worst and chromosome length
    is the the best
    :param individual
    an array if bitwise values (ie 0s or 1s):
    :return: sum of the bitwise values
    """
    return sum(individual),


# set up the toolbox with preset functions from tools package
toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# set population size to 300
population = toolbox.population(n=300)

# run the evolutions
for gen in range(MAX_GEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))
    top2 = tools.selBest(population, k=2)  # printTop(top2)

    if sum(top2[0]) == INDIVIDUAL_LENGTH and TERMINATE_ON_SOLUTION:
        print('solution found, terminated')
        break
    else:
        print(f'generation {gen}, best result {sum(top2[0])} / {INDIVIDUAL_LENGTH}')
        printTop(top2)


top10 = tools.selBest(population, k=10)

print('final ')
printTop(top10)

print("end")
