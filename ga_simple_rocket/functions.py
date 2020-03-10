""":arg
This file is to be used for function for simple rocket
"""
from graphics import Polygon, Point

from ga_simple_rocket import config


def get_rocket_shape(point) -> Polygon:
    tip = point
    bottom_left = Point(point.x + 10, point.y + 20)
    bottom_right = Point(point.x - 10, point.y + 20)
    vertices = [tip, bottom_left, bottom_right]
    shape = Polygon(vertices)
    shape.setFill("black")
    return shape