import numpy as np
from graphics import *

from rocket import Rocket


WINDOW_SIZE = np.array([600, 600])
MAX_COUNT = 25
MAX_GENERATION = 50
REFRESH_RATE = 0.1
TARGET_POSITION = np.array([0.0, 500.0])
ROCKET_SIZE = 20

# Classes

class Population:
    """
    Population will hold a list of Rockets
    and a list of associated instruction on firing a its rockets
    """

    def __init__(self, population_size):
        self.population_size = population_size
        self.rockets = []
        for r in range(population_size):
            self.rockets.append(Rocket(f'rocket{r}', [[0, 1, 1]] * 30 + [[0, 0, 0]] * 92))

    def get_rocket(self, index):
        if self.population_size < index < 0:
            raise IndexError()
        return self.rockets[index]


# Functions

def convert_position(position):
    """
    converts the position to windows position
    :return:
    """
    return position * np.array([1, -1]).astype(dtype=int) + (WINDOW_SIZE // 2 * np.array([1, 2])).astype(dtype=int)


def get_rocket_shape(rocket_position, rocket_direction) -> Polygon:
    a = convert_position(rocket_position)
    p1 = Point(a[0], a[1])
    p2 = Point(a[0] + ROCKET_SIZE, a[1])
    p3 = Point(a[0] + ROCKET_SIZE, a[1] + 2 * ROCKET_SIZE)
    if 270 > rocket_direction > 90:
        vertices = [p1, p2, p3.move(0, ROCKET_SIZE)]
    else:
        vertices = [p1, p2, p3]
    return Polygon(vertices)


def create_target(win):
    target_position = convert_position(TARGET_POSITION)
    Circle(Point(target_position[0], target_position[1]), 10).draw(win)


def init_shapes(win, pop_size):
    for x in range(pop_size):
        new_rocket = Rocket(f'rocket{x}')


    return -1 # list_rockets, list_of_shapes


def main():
    count = 0
    is_finished = False
    population_size = 1
    # create an initial population
    shapes = []
    population = Population(population_size)


    # create the GUI Grapthwin to add graphics to
    win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])  # give title and dimensions

    # add target to GUI window
    create_target(win)
    # initialise the rockets

    for rocket in population.rockets:
        shape = get_rocket_shape(rocket.position, rocket.direction)
        shapes.append(shape)
        shape.draw(win)

    while count < MAX_COUNT and not is_finished:
        print(f"time: {count}")
        time.sleep(REFRESH_RATE)
        for rocket, shape in zip(population.rockets, shapes):
            change = rocket.update(count)
            shape.move(change[0], change[1])
            rocket.print_all()
        count += 1

    # End GUI

    message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()


main()