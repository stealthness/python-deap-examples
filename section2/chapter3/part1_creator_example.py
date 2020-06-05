"""
The purpose of this python script is to demonstrate the creator() function of DEAP to construct a simple developer
class.
"""
from deap import creator, base
from section2.chapter3.employee_class import Employee

print('start')

# using DEAP framework we will extend the Employee class
creator.create("Developer", Employee, position="Developer", programming_langauges=set)

# Normally we use this function to create fitness and individual classes
# The first common use is to create a fitness class that we will extend from a base Fitness class in base module of DEAP

creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# If we wanted instead to minimise the fitness value then we might create instead

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# weights is a tuple, hence the comma, we can also define optimizing more than one objective using degrees of
# importance

creator.create("FitnessCompound", base.Fitness, weights=(1.0, 0.2, -0.5))

# Second common use of the create function is creating an individual class, which will be extended from list class
# and will assign the attribute fitness to be our FitnessMax class that we create earlier

creator.create("Individual", list, fitness=creator.FitnessMax)

print('End')
