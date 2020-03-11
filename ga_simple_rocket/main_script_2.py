"""
Purpose of this file is to separate the visual from ga algoritm.
This is to be done by passing data of the chages of position and replaying them visually
"""
from graphics import Point

from sklearn.utils import Bunch

from ga_simple_rocket.functions import reply_single_rocket, get_rocket_shape
from ga_simple_rocket.simple_rocket_class import SimpleRocket

d = Bunch()
d.name = 'r0'
d.data = []
d.shape = get_rocket_shape(Point(100, 200))

r = SimpleRocket('r0')
r.pos = 200
r.engine_force = -30
r.engine_on = True

for t in range(80):
    if t > 20:
        r.engine_on = False
    if t > 60:
        r.engine_on = True
        r.engine_force = 40
    if t > 70:
        r.engine_on = False
    ds = r.update()
    d.data.append({'ds': ds, 'pos': r.pos})

reply_single_rocket(d)
