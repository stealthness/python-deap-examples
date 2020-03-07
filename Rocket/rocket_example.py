"""
The Purpose of this file is to demonstrate a genetic algorithm example using rocket.
"""
from graphics import *
import numpy as np
from rocket import constants
import random
LOGGING = False


class Rocket:
    """
    Models a rocket
    """

    def __init__(self, name: str):
        self.acceleration = np.array([0.0, 0.0])
        self.velocity = np.array([0.0, 0.0]).copy()
        self.position = constants.INIT_POSITION.copy()
        self.direction = 0
        self.has_exploded = False
        self.name = name
        self.chromosome = [[0,1,0]]*8+[[0,0,0]]*92

    def __str__(self):
        return self.name

    def calculate_new_acceleration(self, i):
        left_engine, main_engine, right_engine = self.chromosome[i]
        new_acceleration = self.acceleration.copy()
        if main_engine == 1:
            new_acceleration += np.array([0, 20]) + np.array([0, constants.GRAVITY])
        return new_acceleration

    def update(self, i) -> np.array:
        self.acceleration = self.calculate_new_acceleration(i)
        print(type(self.velocity[0]))
        self.velocity += self.acceleration/10.0
        self.position += self.velocity.copy()/10.0
        self.check_in_area()
        if LOGGING:
            self.print_all
        return self.velocity.astype(dtype=int) * np.array([1, -1])

    def check_in_area(self):
        if self.position[1] < 0.0:
            print(f'{self.name} has exploded on ground')
            self.has_exploded = True
        if self.position[0] > float(constants.WINDOW_SIZE[0])/2.0 :
            print(f'{self.name} has exploded to the left')
            self.has_exploded = True
        if self.position[1] > float(constants.WINDOW_SIZE[1]):
            print(f'{self.name} has exploded to high')
            self.has_exploded = True

    def check_distance_from(self, target):
        distance = np.sqrt(np.sum((self.position - target)**2))
        print(f'distance is {distance}')
        return distance

    def has_reached_target(self, target):
        if self.check_distance_from(target) < 1:
            print(f'{self.name} has reached its target')
        return self.check_distance_from(target) < 1

    def print_all(self):
        print(f'name: {self.name}, exploded : {self.has_exploded}')
        print(f'pos: {self.position} - vel: {self.velocity} - acc: {self.acceleration}')


def convert_position(position):
    """
    converts the position to windows position
    :return:
    """
    return position * np.array([1, -1]).astype(dtype=int) + (constants.WINDOW_SIZE//2 * np.array([1, 2])).astype(dtype=int)


def get_shape(position) -> Polygon:
    a = convert_position(position)
    p1 = Point(a[0], a[1])
    p2 = Point(a[0] + constants.ROCKET_SIZE, a[1])
    p3 = Point(a[0] + constants.ROCKET_SIZE, a[1] + 2 * constants.ROCKET_SIZE)
    vertices = [p1, p2, p3]
    return Polygon(vertices)


def create_target(win):
    target_position = convert_position(constants.TARGET_POSITION)
    Circle(Point(target_position[0], target_position[1]), 10).draw(win)


def init_shapes(win, pop_size):
    list_rockets = []
    list_of_shapes = []
    for x in range(pop_size):
        new_rocket = Rocket(f'rocket{x}')
        list_rockets.append(new_rocket)
        list_of_shapes.append(get_shape(new_rocket.position))

    for shape in list_of_shapes:
        shape.draw(win)
    return list_rockets, list_of_shapes


def main():
    count = 0
    is_finished = False
    population = []
    population_size = 10

    # create the Grapthwin to add graphics to
    win = GraphWin('Face', constants.WINDOW_SIZE[0], constants.WINDOW_SIZE[1])  # give title and dimensions

    create_target(win)
    rockets, shapes = init_shapes(win, population_size)

    while count < constants.MAX_GENERATION and not is_finished:
        print(f"generation: {count}")
        for shape, rocket in zip(shapes, rockets):
            rocket.print_all()
            if rocket.has_exploded:
                continue
            else:

                change = rocket.update(count)
                shape.move(change[0], change[1])
                if rocket.has_reached_target(constants.TARGET_POSITION):
                    print("win")
                    is_finished = True
                else:
                    print(f"change: {change[0]}, {change[1]}")
                    print(f"x,y: {shape.points[0].getX()},{shape.points[0].getY()}  pos: {rocket.position}")

        time.sleep(constants.REFRESH_RATE)
        count += 1

    message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()


main()
