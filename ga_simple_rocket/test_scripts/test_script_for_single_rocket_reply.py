"""
Purpose of this test script is to create a single individual rocket that will free fall and crash.
A Bunch object is created to store the {time, ds, pos, vel, acc, has_landed, has_failed} details at each time interval
"""
from sklearn.utils import Bunch

from ga_simple_rocket.config import MAX_TIME_INTERVALS
from ga_simple_rocket.functions import reply_single_rocket
from ga_simple_rocket.individual_class import Individual

# creating the bunch object
d = Bunch()
d.name = 'r0'
d.data = []

# creating an individual and initial rocket data
individual = Individual('r0')
individual.rocket.pos = 200
individual.rocket.engine_force = 10
individual.rocket.engine_on = False
info = {'time': 0, 'ds': 0.0, 'pos': individual.rocket.pos, 'vel': individual.rocket.vel, 'acc': individual.rocket.acc}
info.update({'failed': False, 'landed': False})
d.data.append(info)

# Run simulation of the rockets free fall
for t in range(MAX_TIME_INTERVALS):
    ds, _ = individual.update(t)

    info = {'time': t+1, 'ds': ds, 'pos': individual.rocket.pos, 'vel': individual.rocket.vel, 'acc': individual.rocket.acc}
    info.update({'failed': individual.rocket.has_failed, 'landed': individual.rocket.has_landed})
    d.data.append(info)

# visualise the results
reply_single_rocket(d, 300)
