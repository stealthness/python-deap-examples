"""
The purpose of this file is test a single individual rocket
"""
from graphics import *
from typing import List

from ga_simple_rocket.config import *
from ga_simple_rocket.functions import get_rocket_shape, set_rocket_color, get_ground_and_sky_limit
from simple_rocket.individual import Individual

# give title and dimensions
win = GraphWin('Simple Rocket Test', WINDOW_SIZE[0], WINDOW_SIZE[1])

# Create two lines
get_ground_and_sky_limit(win)

shapes: List[Polygon] = []
population: List[Individual] = [Individual('r0')]

# create an individual at start height
population[0].rocket.pos = START_HEIGHT
population[0].commands = [0]*MAX_TIME_INTERVALS
# shape for new_ind
y = - population[0].rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(win.getWidth()/2, y)))

population[0].rocket.vel = 10  # intially moving up
population[0].rocket.acc = 0.0  # free falling

set_rocket_color(population[0].rocket, shapes[0])
shapes[0].draw(win)

# set reference objects
population.append(Individual('r200'))
population[1].rocket.pos = 200
y = - population[1].rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(win.getWidth()/3, y)))
shapes[1].setFill('green')
shapes[1].draw(win)

t = 0
MAX_TIME_INTERVALS = 200
while t < MAX_TIME_INTERVALS:
    time.sleep(REFRESH_RATE)
    ds, fitness = population[0].update(t)
    shapes[0].move(0, -ds)
    t += 1
    print(t)

message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()