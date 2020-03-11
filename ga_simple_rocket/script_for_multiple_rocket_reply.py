"""
Purpose of this file is to separate the visual from ga algoritm.
This is to be done by passing data of the chages of position and replaying them visually
"""
from graphics import Point

from sklearn.utils import Bunch

from ga_simple_rocket.functions import reply_single_rocket, get_rocket_shape, reply_multiple_rocket
from ga_simple_rocket.individual_class import Individual
from ga_simple_rocket.simple_rocket_class import SimpleRocket

number_of_rockets = 5

d = Bunch()
d.names = []
d.rockets = []
individuals = []
for i in range(number_of_rockets):
    name = f'r{i}'
    d.names.append(name)
    individual = Individual(name)
    individual.rocket.engine_force = 20
    individual.rocket.pos = 200
    individuals.append(individual)
    d.rockets.append({f'{individual.rocket.name}': {'ds': 0.0, 'pos': individual.rocket.pos}})

for t in range(120):
    for individual in individuals:
        ds, _ = individual.update(t)
        d.rockets.append({f'{individual.rocket.name}': {'ds': ds, 'pos': individual.rocket.pos}})


reply_multiple_rocket(d)
