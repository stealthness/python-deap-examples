from graphics import *
import random

import numpy as np

from ga_rocket_example import config
from ga_rocket_example.config import ROCKET_SIZE, WINDOW_SIZE, TARGET_POSITION


def get_rocket_shape(center: Point, rocket_direction:int) -> Polygon:
    tip = rotate_about_centre(center, ROCKET_SIZE, rocket_direction)
    bottom_left = rotate_about_centre(center, ROCKET_SIZE // 2, rocket_direction + 120)
    bottom_right = rotate_about_centre(center, ROCKET_SIZE // 2, rocket_direction + 240)
    vertices = [tip, bottom_left, bottom_right]
    shape = Polygon(vertices)
    shape.setFill('black')
    return shape


def convert_position(position):
    """
    converts the position to windows position
    :return:
    """
    return position * np.array([1, -1]).astype(dtype=int) + (WINDOW_SIZE // 2 * np.array([1, 2])).astype(dtype=int)


def convert_position_point(position):
    """
    Converts a numpy  array position into a Point
    :return: Point
    """
    # rescale to Window size
    p = position * np.array([1, -1]).astype(dtype=int) + (WINDOW_SIZE // 2 * np.array([1, 2])).astype(dtype=int)
    return Point(p[0], p[1])


def rotate_about_centre(center: Point, magnitude, rotation):
    return Point(center.x + magnitude * np.sin(2*np.pi*rotation/360), center.y - magnitude * np.cos(2*np.pi*rotation/360))


def rotate_rocket_shape(shape: Polygon, center: Point, direction):
    new_tip = rotate_about_centre(center, ROCKET_SIZE, direction)
    new_bottom_left = rotate_about_centre(center, ROCKET_SIZE // 2, direction + 2 * np.pi / 3)
    new_bottom_right = rotate_about_centre(center, ROCKET_SIZE // 2, direction + 4 * np.pi / 3)
    shape.getPoints()[0].move(shape.getPoints()[0].x - new_tip.x, shape.getPoints()[0].y - new_tip.y)
    shape.getPoints()[1].move(shape.getPoints()[1].x - new_bottom_left.x, shape.getPoints()[1].y - new_bottom_left.y)
    shape.getPoints()[2].move(shape.getPoints()[2].x - new_bottom_right.x, shape.getPoints()[2].y - new_bottom_right.y)


def rotatePolygon(polygon, rotation):
    """Rotates the given polygon which consists of corners represented as (x,y),
    around the ORIGIN, clock-wise"""
    rotation = np.radians(rotation)
    rotated_polygon = []
    for vertices in polygon:
        rotated_polygon.append((vertices[0] * np.cos(rotation) - vertices[1] * np.sin(rotation),
                               vertices[0] * np.sin(rotation) + vertices[1] * np.cos(rotation)))
    return Polygon(rotated_polygon)


def create_target(win):
    target_position = convert_position(TARGET_POSITION)
    Circle(Point(target_position[0], target_position[1]), 10).draw(win)


def create_random_commands():
    commands = []
    i = 0
    engine_configuration = [0.3, 0.6, 0.7, 0.8, 0.9]
    while i < config.MAX_COUNT:
        r = random.random()
        i += 1
        if r <= engine_configuration[0]:
            # 50% of the time fire just main engine
            command = [0,1,0]
        elif r < engine_configuration[1]:
            # 10 % fires the left and main
            command = [1,1,0]
        elif r < engine_configuration[2]:
            # 10 % fires the right and main
            command = [0,1,1]
        elif r < engine_configuration[3]:
            # 10 % fires just the left
            command = [1,0,0]
        elif r < engine_configuration[4]:
            # 10 % fires just the right
            command = [0,0,1]
        else:
            # free fall
            command = [0,0,0]
        commands.append(command)
    return commands
