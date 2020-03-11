"""
Purpose of this file is to separate the visual from ga algoritm.
This is to be done by passing data of the chages of position and replaying them visually
"""
from graphics import Point

from sklearn.utils import Bunch

from ga_simple_rocket.functions import reply_single_rocket, get_rocket_shape
from ga_simple_rocket.individual_class import Individual
from ga_simple_rocket.simple_rocket_class import SimpleRocket

d = Bunch()
d.name = 'r0'
d.data = []

ind = Individual('r0')
ind.rocket
ind.rocket.pos = 200
ind.rocket.engine_force = 10
ind.rocket.engine_on = False
d.data.append({'time': 0, 'ds': 0.0, 'pos': ind.rocket.pos, 'failed': False, 'landed': False})
for t in range(120):
    ds, _ = ind.update(t)
    d.data.append({'time': t+1, 'ds': ds, 'pos': ind.rocket.pos, 'failed': ind.rocket.has_failed, 'landed': ind.rocket.has_landed})

reply_single_rocket(d, 300)
