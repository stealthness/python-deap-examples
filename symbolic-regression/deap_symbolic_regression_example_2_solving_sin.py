import math
import operator
import random
import matplotlib.pyplot as plt
import numpy as np
from deap import algorithms, base, creator, tools, gp

# Set Parameters (default values in comments)
# MAX_GEN = 100
# CXPB = 0.5
# MUTPB = 0.1
# MAX_VALUE = 17

MAX_GEN = 100
CXPB = 0.5
MUTPB = 0.1
MAX_VALUE = 25
POINTS = [math.pi*x/10 for x in range(-10, 10)]
ADJ = 0.1*math.pi
random.seed(318)

# Set function want to find

# Defince the expected function
def exp_function(x):
    return math.sin(x)


# Define new functions
def protected_div(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1


# Set our constants(terminals) and primitives(functions) set
pset = gp.PrimitiveSet("MAIN", 1)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(protected_div, 2, name="div")
pset.addPrimitive(operator.neg, 1)
pset.addEphemeralConstant("randfactorial", lambda: math.factorial(random.randint(0, 7)))
pset.renameArguments(ARG0='x')

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=4)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

def evalSymbReg(individual, points):
    # Transform the tree expression in a callable function
    evl_func = toolbox.compile(expr=individual)
    # Evaluate the mean squared error between the expression
    # and the real function f(x): defined above
    sqr_errors = ((evl_func(x) - exp_function(x))**2 for x in points)
    return math.fsum(sqr_errors) / len(points),


toolbox.register("evaluate", evalSymbReg, points=POINTS)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=MAX_VALUE))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=MAX_VALUE))

print('start')

pop = toolbox.population(n=300)
hof = tools.HallOfFame(1)

# creating mstats to record evolution data

stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
stats_size = tools.Statistics(len)
mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
mstats.register("avg", np.mean)
mstats.register("std", np.std)
mstats.register("min", np.min)
mstats.register("max", np.max)

# print log
pop, log = algorithms.eaSimple(pop, toolbox, CXPB, MUTPB, MAX_GEN, stats=mstats, halloffame=hof, verbose=True)

print("\nBest expression found is;")
print(hof[0])

# creating graph using matplotlib
exp_func_points = [exp_function(x) for x in POINTS]
plt.plot(POINTS, exp_func_points, label='Expected function')

evl_func = toolbox.compile(expr=hof[0])
eval_func_points  = [evl_func(x) for x in POINTS]
plt.plot(POINTS, eval_func_points , label='Evaluated function')
plt.legend()
plt.plot()
plt.show()

print('end')