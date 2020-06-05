#    This file is part of EAP.
#
#    EAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    EAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with EAP. If not, see <http://www.gnu.org/licenses/>.
"""
The purpose of this file is to demonstrate an example of using DEAP genetic programming to solve a symbolic polynomial

The example used is x^4 - 2x^3 - x^2 -x

The GP will use a simple set of function +, -, * and  protected divisions
"""
import operator
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from deap import algorithms, base, creator, tools, gp
from utils import protectedDiv
# set parameters

MAX_GENERATION = 50
CXPB = 0.6
MUTPB = 0.1
POINTS = [x / 10. for x in range(-10, 10)]
random.seed(318)


# definc
def exp_function(x):
    return (x ** 4) - 2 * (x ** 3) - (x ** 2) - x





# creating pset which is a set primitives that will contain the terminal and function nodes of expression tree
pset = gp.PrimitiveSet("MAIN", 1)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2, )
pset.addPrimitive(protectedDiv, 2, "div")
pset.addEphemeralConstant("rand202", lambda: random.randint(-2, 2))
pset.renameArguments(ARG0='x')

# creator is used to create initial expression trees
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)


def evalSymbReg(individual, points):
    # Transform the tree expression in a callable function
    function = toolbox.compile(expr=individual)
    # Evaluate the mean squared error between the expression
    # and the real function f(x): defined above
    squared_errors = ((function(x) - exp_function(x)) ** 2 for x in points)
    return math.fsum(squared_errors) / len(points),


toolbox.register("evaluate", evalSymbReg, points=POINTS)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

print('start')
# fix the random seed
random.seed(42)

# set population to 300
pop = toolbox.population(n=300)
hof = tools.HallOfFame(1)

stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
stats_size = tools.Statistics(len)
mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
mstats.register("avg", np.mean)
mstats.register("std", np.std)
mstats.register("min", np.min)
mstats.register("max", np.max)
pop, log = algorithms.eaSimple(pop, toolbox, CXPB, MUTPB, MAX_GENERATION, stats=mstats, halloffame=hof)

print(hof[0])

exp_function_points = [exp_function(x) for x in POINTS]
plt.plot(POINTS, exp_function_points, label='f')

act_function = toolbox.compile(expr=hof[0])
f_points = [act_function(x) for x in POINTS]
plt.plot(POINTS, f_points, label='f')
plt.plot()

plt.show()
# print log
print('end')
