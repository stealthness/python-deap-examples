import numpy as np
import logging

from ga_rocket_example.config import *


class Rocket:
    """
    Models a rocket
    """

    def __init__(self, name: str, chromosome):
        self.name = name
        self.acceleration = np.array([0.0, 0.0])
        self.velocity = np.array([0.0, 0.0])
        self.position = np.array(START_POSITION, dtype=float)
        self.direction: int = 0
        self.main_engine_on = True
        self.main_engine_max_force: int = ROCKET_MAIN_ENGINE_FORCE
        self.rotational_engine_force = ROCKET_ROTATIONAL_ENGINE_FORCE
        self.time_interval = 1 / TIME_INTERVALS_PER_SEC
        self.has_exploded = False
        self.verbose = True
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(f'Rocket:{name}')

    def __str__(self):
        return self.name

    def update(self, command) -> np.array:
        if self.has_exploded:
            self.logger.debug(f'No update - Rocket has exploded')
            return np.array((0, 0), dtype=float)
        else:
            # update direction
            self.calculate_new_direction(command)
            # update acceleration, engine is on if commands[1] == 1
            if command[1] == 1:
                self.main_engine_on = True
            self.calculate_new_acceleration()
            # update velocity
            self.velocity += self.acceleration.copy() / self.time_intervals
            # update position
            self.position += self.velocity.copy() / self.time_intervals
            self.check_in_area()

            # return the change in position
            self.logger.debug(f'pos: {self.position}, vel: {self.velocity}, acc {self.acceleration}')
        return self.velocity.astype(dtype=int) * np.array([1, -1])

    def check_in_area(self):
        if self.position[1] < GROUND_LEVEL:
            self.logger.debug(f'Crashed on the ground')
            self.has_exploded = True
        if np.abs(self.position[0]) > MAX_HORIZONTAL_DEVIATION:
            self.logger.debug(f'Gone off the side')
            self.has_exploded = True
        if self.position[1] > float(MAX_HEIGHT):
            self.logger.debug(f'Gone too high')
            self.has_exploded = True

    def check_distance_from(self, target):
        distance = np.sqrt(np.sum((self.position - target)**2))
        self.logger.debug(f'distance is {distance}')
        return distance

    def has_reached_target(self, target):
        if self.check_distance_from(target) < 1:
            self.logger.debug(f'Target reached')
        return self.check_distance_from(target) < 1

    # Calculation the the Rockets change

    def calculate_new_acceleration(self):
        """
        Calculates the change in acceleration
        """
        new_acceleration = self.acceleration.copy()
        if self.main_engine_on:
            rocket_acc = np.array([np.sin(self.direction), np.cos(self.direction)]) * self.main_engine_max_force
            new_acceleration = self.acceleration + GRAVITY + rocket_acc
        else:
            new_acceleration = self.acceleration + GRAVITY
        return new_acceleration.copy()

    def calculate_new_direction(self, commands):
        """
        calculates the new direction of the rocket
        :param commands:
        """
        if commands[0] == 1 and commands[2] == 0:
            self.logger.debug(f'Fire left engine')
            self.direction += ROCKET_ROTATIONAL_ENGINE_FORCE
        elif commands[0] == 0 and commands[2] == 1:
            self.logger.debug(f'Fire left engine')
            self.direction -= ROCKET_ROTATIONAL_ENGINE_FORCE
        else:
            print('no turn')

    # DEBUG TOOLS

    def print_all(self):
        print(f'name: {self.name}, exploded : {self.has_exploded}')
        print(f'pos: {self.position} - vel: {self.velocity} - acc: {self.acceleration} - dir: {self.direction}')