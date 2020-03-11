"""
This is test code for simple rocket shape
"""
from graphics import *
from typing import List

from ga_simple_rocket.config import *
from ga_simple_rocket.functions import get_rocket_shape, set_rocket_color, get_ground_and_sky_limit

# create the GUI Grapthwin to add graphics to
from ga_simple_rocket.individual_class import Individual

# give title and dimensions
win = GraphWin('Simple Rocket Test', WINDOW_SIZE[0], WINDOW_SIZE[1])

# Create two lines
get_ground_and_sky_limit(win)

shapes: List[Polygon] = []
population: List[Individual] = []

# create an individual at start height
new_ind = Individual("r0")
new_ind.rocket.pos = START_HEIGHT
population.append(new_ind)
# shape for new_ind
y = - new_ind.rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(50, y)))

# create an individual at ground, but at speed
new_ind = Individual("r1")
new_ind.rocket.pos = GROUND_LEVEL
new_ind.rocket.vel = -20
new_ind.rocket.acc = -9.8
new_ind.rocket.has_failed = True
population.append(new_ind)
y = - new_ind.rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(100, y)))

# create an individual at ground, but at rest
new_ind = Individual("r2")
new_ind.rocket.pos = GROUND_LEVEL
new_ind.rocket.vel = 0.0001
new_ind.rocket.acc = 0.02
new_ind.rocket.has_landed = True
population.append(new_ind)
y = - new_ind.rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(150, y)))

# create an individual at ground, but at rest
new_ind = Individual("r3")
new_ind.rocket.vel = 25.0
new_ind.rocket.pos = MAX_ROCKET_HEIGHT + new_ind.rocket.vel + 10
new_ind.rocket.acc = 50
new_ind.rocket.has_failed = True
population.append(new_ind)
y = - new_ind.rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(200, y)))


# create an individual at start height
new_ind = Individual("r4")
new_ind.rocket.pos = START_HEIGHT
new_ind.rocket.engine_on = True
population.append(new_ind)
y = - new_ind.rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(250, y)))

for shape, ind in zip (shapes, population):
    set_rocket_color(ind.rocket, shape)
    shape.draw(win)


message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()