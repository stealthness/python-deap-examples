""":arg
This file is to be used for function for simple rocket
"""
from graphics import Polygon, Point, Line, Text, GraphWin, time
from random import random, uniform

from sklearn.utils import Bunch

from ga_simple_rocket.config import MAX_ROCKET_HEIGHT, WIN_ADJUST, WINDOW_SIZE, REFRESH_RATE, ROCKET_SIZE
from ga_simple_rocket.individual_class import Individual
from ga_simple_rocket.simple_rocket_class import SimpleRocket


def get_rocket_shape(point) -> Polygon:
    point.move(0, -ROCKET_SIZE)
    tip = point
    bottom_left = Point(point.x + ROCKET_SIZE//2, point.y + ROCKET_SIZE)
    bottom_right = Point(point.x - ROCKET_SIZE//2, point.y + ROCKET_SIZE)
    vertices = [tip, bottom_left, bottom_right]
    shape = Polygon(vertices)
    shape.setFill("black")
    return shape


def set_rocket_color(rocket: SimpleRocket, shape):
    if rocket.has_failed:
        shape.setFill('red')
    elif rocket.has_landed:
        shape.setFill('green')
    elif rocket.engine_on:
        shape.setFill('gray')
    else:
        shape.setFill('black')


def get_ground_and_sky_limit(win):
    y = win.getHeight() - WIN_ADJUST
    line = Line(Point(0, y), Point(win.getWidth(), y))
    line.draw(win)

    y = win.getHeight() - MAX_ROCKET_HEIGHT - WIN_ADJUST
    line = Line(Point(0, y), Point(win.getWidth(), y))
    line.setFill('red')
    line.draw(win)


def end_windows(win):
    """
    Boiler plate code to end window
    :param win:
    :return:
    """
    message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()


def reply_single_rocket(b: Bunch, x: int = 100) -> object:
    """
    Animates the the data of a single rocket falling
    :param b: Bunch object holding data information
    :param x: position  horizontally along the screen, default 100
    :return:
    """
    win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])
    get_ground_and_sky_limit(win)
    # create rocket shape from the initial rocket position
    y = win.getHeight() - WIN_ADJUST - b.data[0]['pos']
    shape = get_rocket_shape(Point(x, y))
    shape.draw(win)
    # create time counter
    time_message = Text(Point(win.getWidth() / 4, win.getHeight() - 20), 'time:0')
    time_message.draw(win)
    # animate using the data
    for i, d in enumerate(b.data):
        time.sleep(REFRESH_RATE)
        shape.move(0, -d['ds'])
        color_shape(shape, d['failed'], d['landed'])
        time_message.setText(f'time:{i+1}')
    end_windows(win)


def reply_multiple_rocket(b: Bunch):
    """
    Will draw multiple rockets evenly space and reply their movement
    :param b: Bunch object holding data information
    """
    win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])
    get_ground_and_sky_limit(win)
    # create time counter
    time_message = Text(Point(win.getWidth() / 4, win.getHeight() - 20), 'time:0')
    time_message.draw(win)
    shapes = []
    n = len(b.data)
    for i in range(n):
        print(f'create shape{i}')
        # create rocket shape from the initial rocket position
        y = win.getHeight() - WIN_ADJUST - b.data[0][0]['pos']
        x = win.getWidth()/(n+1)
        shapes.append(get_rocket_shape(Point(x + x*i, y)))
        shapes[i].draw(win)

    for t in range(100):
        time.sleep(REFRESH_RATE)
        for i in range(n):
            ds = b.data[i][t]['ds']
            shapes[i].move(0, -ds)
            color_shape(shapes[i], b.data[i][t]['failed'], b.data[i][t]['landed'])
        time_message.setText(f'time:{i+1}')

    end_windows(win)


def color_shape(shape, has_failed, has_landed):
    if has_failed:
        shape.setFill('red')
    elif has_landed:
        shape.setFill('green')


def select_roulette(individuals, k):
    sorted_inds = sorted(individuals, reverse=True)
    sum_fits = sum(ind.fitness[0] for ind in individuals)
    chosen = []
    for i in range(k):
        r = uniform(0, sum_fits)
        sum_ = 0
        for ind in sorted_inds:
            sum_ += ind.fitness[0]
            if sum_ > r:
                chosen.append(ind)
                break

    return chosen


def mutate_individual(individual: Individual, indpb: float):
    for i in range(len(individual.commands)):
        if random() < indpb:
            individual.commands[i] = type(individual.commands[i])(not individual.commands[i])
    return individual,


def fitness_function_simple(rocket, t, max_t) -> float:
    """
    Calculates the the fitness of the rocket position from the target location
        if rocket has failed:
            then fitness is 1.0
        if rocket has succeeded:
            then fitness will be 0.0 + relative time taken
            relative time will be  1.0 - t / max_time
    :param: time
    :param: max time allowed
    :return: fitness of the individual
    """
    if rocket.has_failed():
        rocket.fitness = 1.0
    elif rocket.has_landed():
        if t == 0:
            rocket.fitness = 0.0
        else:
            rocket.fitness = 1.0 - t / max_t
    else:
        rocket.fitness = 1.0 - t / max_t
    return rocket.fitness
