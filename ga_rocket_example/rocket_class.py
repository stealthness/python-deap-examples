import numpy as np
import logging

from ga_rocket_example.config import *


class Rocket:
    """
    Models a rocket
    """

    def __init__(self, name: str):
        self.name = name
        self.acc = np.array([0.0, 0.0])
        self.vel = np.array([0.0, 0.0])
        self.pos = np.array(START_POSITION, dtype=float)
        self.dir: int = 0
        self.main_engine_on = True
        self.main_engine_max_force: int = ROCKET_MAIN_ENGINE_FORCE
        self.rotational_engine_force = ROCKET_ROTATIONAL_ENGINE_FORCE
        self.time_interval = 1 / TIME_INTERVALS_PER_SEC
        self.has_failed = False
        # logging info
        self.verbose = True
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(f'Rocket:{name}')

    def __str__(self):
        return self.name

    def update(self, command) -> np.array:
        if self.has_failed:
            self.logger.debug(f'No update - Rocket has exploded')
            return 0.0, 0.0
        else:
            delta_time = 1.0 / float(TIME_INTERVALS_PER_SEC)

            # update direction
            self.calculate_new_direction(command)

            # update acceleration, engine is on if commands[1] == 1
            if command[1] == 1:
                self.main_engine_on = True
            dr = self.calculate_new_acceleration()

            # update velocity
            self.vel += self.acc.copy() / delta_time
            dvx = self.acc[0] * delta_time
            dvy = self.acc[1] * delta_time

            # update position
            dx = (self.vel[0] - self.acc[0] * delta_time/2) * delta_time
            dy = (self.vel[1] - self.acc[1] * delta_time/2) * delta_time
            self.pos += np.array([dx, dy])

            self.check_in_area()

            # return the change in position
            self.logger.debug(f'pos: {self.pos}, vel: {self.vel}, acc {self.acc}')
        return dx, dy, dr

    def check_in_area(self):
        if self.pos[1] < GROUND_LEVEL:
            self.logger.debug(f'Crashed on the ground')
            self.has_exploded = True
        if np.abs(self.pos[0]) > MAX_HORIZONTAL_DEVIATION:
            self.logger.debug(f'Gone off the side')
            self.has_exploded = True
        if self.pos[1] > float(MAX_ROCKET_HEIGHT):
            self.logger.debug(f'Gone too high')
            self.has_exploded = True

    def check_distance_from(self, target):
        distance = np.sqrt(np.sum((self.pos - target) ** 2))
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
        new_acceleration = self.acc.copy()
        if self.main_engine_on:
            rocket_acc = np.array([np.sin(self.dir), np.cos(self.dir)]) * self.main_engine_max_force
            new_acceleration = self.acc + GRAVITY + rocket_acc
        else:
            new_acceleration = self.acc + GRAVITY
        return new_acceleration

    def calculate_new_direction(self, command):
        """
        calculates the new direction of the rocket
        :param command:
        """
        if command[0] == 1 and command[2] == 0:
            self.logger.debug(f'Fire left engine')
            self.dir += ROCKET_ROTATIONAL_ENGINE_FORCE
            return ROCKET_ROTATIONAL_ENGINE_FORCE
        elif command[0] == 0 and command[2] == 1:
            self.logger.debug(f'Fire left engine')
            self.dir -= ROCKET_ROTATIONAL_ENGINE_FORCE
            return -ROCKET_ROTATIONAL_ENGINE_FORCE
        else:
            return 0

    # DEBUG TOOLS

    def print_all(self):
        print(f'name: {self.name}, exploded : {self.has_exploded}')
        print(f'pos: {self.pos} - vel: {self.vel} - acc: {self.acc} - dir: {self.dir}')