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

number_of_rockets = 2

# creating a Bunch object to store individuals details
b = Bunch()
b.names = ['r0', 'r1']
individuals = [Individual('r0'), Individual('r1')]

# creating two rockets
b.rockets = [individuals[0].rocket, individuals[1].rocket]
r0_data = []
r1_data = []
individuals[1].commands = [0]*MAX_TIME_INTERVALS



b.data = [r0_data, r1_data]

b.rockets[0].pos = 200
b.rockets[1].pos = 200

for i in range(number_of_rockets):
    info = {'time': 0, 'ds': 0.0, 'pos': b.rockets[i].pos, 'vel': b.rockets[i].vel, 'acc': b.rockets[i].acc}
    info.update({'failed': False, 'landed': False})
    b.data[i].append(info)

    for t in range(MAX_TIME_INTERVALS):
        ds, fitness = individuals[i].update(t)

        is_landed = b.rockets[i].has_landed
        is_failed = b.rockets[i].has_failed
        info = {'time': 0, 'ds': ds, 'pos': b.rockets[i].pos, 'vel': b.rockets[i].vel, 'acc': b.rockets[i].acc}
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
