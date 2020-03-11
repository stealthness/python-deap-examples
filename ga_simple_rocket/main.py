"""
This is the main code for the simple rocket example
"""
from graphics import *
from random import random

from ga_simple_rocket.config import *
from ga_simple_rocket.functions import get_rocket_shape, set_rocket_color, get_ground_and_sky_limit
from simple_rocket.individual import Individual

# create the GUI Grapthwin to add graphics to
win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])  # give title and dimensions

ground_level = WINDOW_SIZE[1] - WIN_ADJUST
population = []
shapes = []

for x in range(POPULATION_SIZE):
    individual = Individual(f'r{x}')
    individual.rocket.pos = START_HEIGHT
    individual.rocket.engine_force = ROCKET_ENGINE_FORCE
    population.append(individual)

all_off = [0]*MAX_TIME_INTERVALS
all_on = [1]*MAX_TIME_INTERVALS

population[0].commands = all_off
population[0].rocket.engine_force = 100

x = 76
y = 35
population[1].commands = [0]*x + [1]*y + [0]*(MAX_TIME_INTERVALS - x - y)
population[1].rocket.engine_force = 33

population[2].commands = all_on
population[2].rocket.engine_force = 20

x = (win.getWidth() - 20) / POPULATION_SIZE
for ind in population:
    y = - ind.rocket.pos - WIN_ADJUST + win.getHeight()
    shape = get_rocket_shape(Point(x, y))
    shape.draw(win)
    shapes.append(shape)
    x += (win.getWidth() - 20) / POPULATION_SIZE

# set time interval to 0
t = 0
info_msg = Text(Point(win.getWidth() - 100, win.getWidth() - 100), f't is {t} pos:{population[0].rocket.pos}')
info_msg.draw(win)

get_ground_and_sky_limit(win)
solution_found = False
solution_possible = True
while t < MAX_TIME_INTERVALS and solution_possible:
    solution_possible = False
    time.sleep(REFRESH_RATE)
    for shape, ind in zip(shapes, population):
        ds, fitness = ind.update(t)
        shape.move(0, -ds)
        set_rocket_color(ind.rocket, shape)
        if ind.has_landed():
            print("solution found")
            solution_found = True
            set_rocket_color(ind.rocket, shape)
        elif not ind.has_failed():
            solution_possible = True
        elif ind.has_failed():
            set_rocket_color(ind.rocket, shape)

    info_msg.setText(f't is {t} pos:{population[0].rocket.pos:0.4f}')
    t += 1

# End GUI

print(f"time {t}")
message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()