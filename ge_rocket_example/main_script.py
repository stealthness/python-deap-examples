from rocket.rocket import Rocket
import numpy as np
from rocket.population import Population
from ge_rocket_example.functions import *
from graphics import *
from ge_rocket_example.config import MAX_COUNT

rocket = Rocket('test1', [[0, 1, 0]]*1)
rockets = []
for x in range(10):
    commands = [[0,1,0]]*10 + create_random_commands()
    rockets.append(Rocket(f'r{x}', commands))
print(rocket.name)

count = 0
is_finished = False
population_size = 1
# create an initial population
shapes = []
population = Population(population_size)
population.rockets = rockets


# create the GUI Grapthwin to add graphics to
win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])  # give title and dimensions

# add target to GUI window
create_target(win)
# initialise the rockets

for rocket in population.rockets:
    shape = get_rocket_shape(rocket.position, rocket.direction)
    shapes.append(shape)
    shape.draw(win)

while count < MAX_COUNT and not population.has_finished():
    print(f"time: {count}")
    time.sleep(REFRESH_RATE)
    for rocket, shape in zip(population.rockets, shapes):
        change = rocket.update(count)
        rotate_rocket_shape(shape, convert_position_point(rocket.position), rocket.direction)
        shape.move(change[0], change[1])
        rocket.print_all()
    count += 1

# End GUI

message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()
