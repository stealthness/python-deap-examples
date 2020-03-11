"""
Purpose of this test script is to create two individual rockets that will free fall and crash.
A Bunch object is created to store the {time, ds, pos, vel, acc, has_landed, has_failed} details at each time interval
"""
from graphics import Point

from sklearn.utils import Bunch

from ga_simple_rocket.config import MAX_TIME_INTERVALS
from ga_simple_rocket.functions import reply_single_rocket, get_rocket_shape, reply_multiple_rocket
from ga_simple_rocket.individual_class import Individual
from ga_simple_rocket.simple_rocket_class import SimpleRocket

number_of_rockets = 5

# creating a Bunch object to store individuals details
b = Bunch()
b.names = []
b.individuals = []
b.data = []
for i in range(number_of_rockets):
    b.names.append(f'r{i}')
    b.individuals.append(Individual(f'r{i}'))
    b.individuals[i].rocket.pos = 200
    b.data.append([])

    info = {'time': 0, 'ds': 0.0}
    info.update({'pos': b.individuals[i].rocket.pos, 'vel': b.individuals[i].rocket.vel, 'acc': b.individuals[i].rocket.acc})
    info.update({'failed': False, 'landed': False})
    b.data[i].append(info)

for i in range(number_of_rockets):
    for t in range(MAX_TIME_INTERVALS):
        ds, fitness = b.individuals[i].update(t)

        is_landed = b.individuals[i].rocket.has_landed
        is_failed = b.individuals[i].rocket.has_failed
        info = {'time': t, 'ds': ds}
        info.update({'pos': b.individuals[i].rocket.pos, 'vel': b.individuals[i].rocket.vel, 'acc': b.individuals[i].rocket.acc})
        info.update({'failed': is_failed, 'landed': is_landed})
        b.data[i].append(info)

# for i in range(number_of_rockets):
#     name = f'r{i}'
#     b.names.append(name)
#     individual = Individual(name)
#     individual.rocket.engine_force = 20
#     individual.rocket.pos = 200
#     individuals.append(individual)
#     b.data.append({name: []})
#     b.rockets.append({f'{individual.rocket.name}': {'ds': 0.0, 'pos': individual.rocket.pos}})
#
# for t in range(120):
#     for individual in individuals:
#         ds, _ = individual.update(t)
#         b.rockets.append({f'{individual.rocket.name}': {'ds': ds, 'pos': individual.rocket.pos}})
#         b.data.append([1])

reply_multiple_rocket(b)
