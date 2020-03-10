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
population[0].rocket.engine_force = 9.8

population[1].commands = all_on
population[1].rocket.engine_force = 9.8

population[2].commands = all_on
population[2].rocket.engine_force = 14

x = (win.getWidth() - 20) / POPULATION_SIZE
for ind in population:
    y = - ind.rocket.pos - WIN_ADJUST + win.getHeight()
    shape = get_rocket_shape(Point(x, y))
    shape.draw(win)
    shapes.append(shape)
    x += (win.getWidth() - 20) / POPULATION_SIZE

# set time interval to 0
t = 0
info_msg = Text(Point(win.getWidth() - 30, win.getWidth() - 30), f'{population[0].rocket.pos}')
info_msg.draw(win)

get_ground_and_sky_limit(win)
solution_found = False
solution_possible = True
while t < MAX_TIME_INTERVALS and solution_possible:
    time.sleep(REFRESH_RATE)
    for shape, ind in zip(shapes, population):
        dv, fitness = ind.update(t)
        shape.move(0, -dv)
        info_msg.setText(f'{population[0].rocket.pos:0.4f}')
        set_rocket_color(ind.rocket, shape)
    for ind in population:
        solution_possible = False
        if ind.has_landed():
            solution_found = True
            break
        elif not ind.has_failed():
            solution_possible = True
            break


# End GUI

    t += 1
message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()