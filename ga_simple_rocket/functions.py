""":arg
This file is to be used for function for simple rocket
"""
from graphics import Polygon, Point, Line, Text, GraphWin, time

from sklearn.utils import Bunch

from ga_simple_rocket.config import MAX_ROCKET_HEIGHT, WIN_ADJUST, WINDOW_SIZE, REFRESH_RATE
from ga_simple_rocket.simple_rocket_class import SimpleRocket


def get_rocket_shape(point) -> Polygon:
    tip = point
    bottom_left = Point(point.x + 10, point.y + 20)
    bottom_right = Point(point.x - 10, point.y + 20)
    vertices = [tip, bottom_left, bottom_right]
    shape = Polygon(vertices)
    shape.setFill("black")
    return shape


def set_rocket_color(rocket:SimpleRocket, shape):
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

def reply_single_rocket(b: Bunch):
    """
    Animates the the data of a single rocket falling
    :param b:
    :return:
    """
    win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])
    get_ground_and_sky_limit(win)
    # create rocket shape from the initial rocket position
    y = win.getHeight() - WIN_ADJUST - b.data[0]['pos']
    shape = get_rocket_shape(Point(100, y))
    shape.draw(win)
    # create time counter
    time_message = Text(Point(win.getWidth() / 4, win.getHeight() - 20), 'time:0')
    time_message.draw(win)
    # animate using the data
    for i, d in enumerate(b.data):
        time.sleep(REFRESH_RATE)
        shape.move(0, -d['ds'])
        time_message.setText(f'time:{i+1}')

    end_windows(win)
