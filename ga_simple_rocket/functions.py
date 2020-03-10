""":arg
This file is to be used for function for simple rocket
"""
from graphics import Polygon, Point

from ga_simple_rocket import config


def get_rocket_shape(position, window_position) -> Polygon:
    x = window_position.x
    y = config.WINDOW_SIZE[0] - position + window_position.y
    tip = Point(x, y)
    bottom_left = Point(x + 10, y + 20)
    bottom_right = Point(x - 10, y + 20)
    vertices = [tip, bottom_left, bottom_right]
    return Polygon(vertices)