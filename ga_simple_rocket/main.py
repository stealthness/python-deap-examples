"""
This is the main code for the simple rocket example
"""
from graphics import *
from random import random

from ga_simple_rocket.config import *
from ga_simple_rocket.functions import get_rocket_shape
from simple_rocket.individual import Individual

# create the GUI Grapthwin to add graphics to
win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])  # give title and dimensions

ground_level = WINDOW_SIZE[1] - WIN_ADJUST
population = []
shapes = []

for x in range(POPULATION_SIZE):
    population.append(Individual(f'r{x}'))

population[1].rocket.engine_on = True
population[1].rocket.engine_force = 9.8

population[2].rocket.engine_on = True
population[2].rocket.engine_force = 14

x = (win.getWidth() - 20) / POPULATION_SIZE
for ind in population:
    ind.rocket.pos = START_HEIGHT
    shape = get_rocket_shape(ind.rocket.pos, Point(x, win.getHeight() - START_HEIGHT - WIN_ADJUST))
    shape.draw(win)
    shapes.append(shape)
    x += (win.getWidth() - 20) / POPULATION_SIZE


t = 0
info_msg = Text(Point(win.getWidth() - 30, win.getWidth() - 30), f'{population[0].rocket.pos}')
info_msg.draw(win)

line = Line(Point(0, win.getHeight()-50), Point(win.getWidth(), win.getHeight()-50))
line.draw(win)

while t < MAX_TIME_INTERVALS:
    time.sleep(REFRESH_RATE)
    for shape, ind in zip(shapes, population):
        dv, fitness = ind.update(t)
        shape.move(0, -dv)
        info_msg.setText(f'{ind.rocket.pos:0.4f}')

        if ind.rocket.name == 'r3':
            ind.rocket.engine_on = (random() < 0.7)
            print(ind.rocket.engine_on)

        if ind.has_landed():
            landed_msg = Text(Point(300, 200), 'Touchdown')
            landed_msg.draw(win)
            break
        elif ind.rocket.has_failed:
            bang_msg = Text(Point(300, 200), 'Bang')
            bang_msg.draw(win)
            break
# End GUI

    t += 1
message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()