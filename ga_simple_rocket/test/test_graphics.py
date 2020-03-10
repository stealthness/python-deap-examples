"""
This is test code for simple rocket shape
"""
from graphics import *

from ga_simple_rocket.config import *
from ga_simple_rocket.functions import get_rocket_shape, set_rocket_color, get_ground_and_sky_limit

# create the GUI Grapthwin to add graphics to
from simple_rocket.individual import Individual

# give title and dimensions
win = GraphWin('Simple Rocket Test', WINDOW_SIZE[0], WINDOW_SIZE[1])

# Create two lines

get_ground_and_sky_limit(win)

shapes = []
population = []

# create an individual at start height
population.append(Individual("r0"))
population[0].rocket.pos = START_HEIGHT
y = - population[0].rocket.pos - WIN_ADJUST + win.getHeight()
print(population[0])
shapes.append(get_rocket_shape(Point(50, y)))

# create an individual at ground, but at speed
population.append(Individual("r1"))
population[1].rocket.pos = GROUND_LEVEL
population[1].rocket.vel = -20
population[1].rocket.acc = -9.8
population[1].rocket.has_failed = True
y = - population[1].rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(100, y)))

# create an individual at ground, but at rest
population.append(Individual("r2"))
population[2].rocket.pos = GROUND_LEVEL
population[2].rocket.vel = 0.0001
population[2].rocket.acc = 0.02
population[2].rocket.has_landed = True
y = - population[2].rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(150, y)))


# create an individual at ground, but at rest
population.append(Individual("r3"))
population[3].rocket.vel = 25.0
population[3].rocket.pos = MAX_ROCKET_HEIGHT + population[3].rocket.vel + 10
population[3].rocket.acc = 50
population[3].rocket.has_failed =  True
y = - population[3].rocket.pos - WIN_ADJUST + win.getHeight()
shapes.append(get_rocket_shape(Point(200, y)))


# create an individual at start height
population.append(Individual("r4"))
population[4].rocket.pos = START_HEIGHT
population[4].rocket.engine_on = True
y = - population[4].rocket.pos - WIN_ADJUST + win.getHeight()
print(population[4])
shapes.append(get_rocket_shape(Point(250, y)))

for shape, ind in zip (shapes, population):
    set_rocket_color(ind.rocket, shape)
    shape.draw(win)


message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()