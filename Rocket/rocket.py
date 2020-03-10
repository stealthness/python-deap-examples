import numpy as np
import logging

ZERO = np.array([0.0, 0.0])
GRAVITY = np.array([0, -9.8])
INIT_POSITION = np.array([0.0, 40.0])
ROCKET_ROTATION_STRENGTH = 0.1
ROCKET_MAIN_STRENGTH = 15
GROUND_LEVEL = 0
MAX_HEIGHT = 800
MAX_HORIZONTAL_DEVIATION = 400
TIME_INTERVALS = 10
REFRESH_RATE = 1/TIME_INTERVALS

class Rocket:
    """
    Models a rocket
    """

    def __init__(self, name: str, chromosome):
        self.acceleration = ZERO.copy()
        self.velocity = ZERO.copy()
        self.position = INIT_POSITION.copy()
        self.direction = 0
        self.main_engine_max_force = ROCKET_MAIN_STRENGTH
        self.rotational_engine_force = ROCKET_ROTATION_STRENGTH
        self.time_intervals = TIME_INTERVALS
        self.has_exploded = False
        self.name = name
        self.chromosome = chromosome
        self.verbose = False
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(f'Rocket:{name}')

    def __str__(self):
        return self.name

    def update(self, i) -> np.array:
        if self.has_exploded:
            self.logger.debug(f'No update - Rocket has exploded')
        else:
            # get commands from chromosome
            commands = self.chromosome[i]

            # update direction
            self.calculate_new_direction(commands)

            # update acceleration, engine is on if commands[1] == 1
            self.acceleration = self.calculate_new_acceleration(commands[1] == 1)
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

    def calculate_new_acceleration(self, engine_on):
        """
        Calculates the change in acceleration
        """
        new_acceleration = self.acceleration.copy()
        if engine_on:
            rocket_acc = np.array([np.sin(self.direction), np.cos(self.direction)]) * self.main_engine_max_force
            new_acceleration = self.acceleration.copy() + GRAVITY + rocket_acc
            print(f"ENGINE ON ----- {new_acceleration} = (a) {self.acceleration} + (g) {GRAVITY} + (e) {rocket_acc}")
        else:
            print('FREE FALL ------')
            new_acceleration = self.acceleration.copy() + GRAVITY
        return new_acceleration.copy()

    def calculate_new_direction(self, commands):
        """
        calculates the new direction of the rocket
        :param commands:
        """
        if commands[0] == 1 and commands[2] == 0:
            self.logger.debug(f'Fire left engine')
            self.direction += ROCKET_ROTATION_STRENGTH
        elif commands[0] == 0 and commands[2] == 1:
            self.logger.debug(f'Fire left engine')
            self.direction -= ROCKET_ROTATION_STRENGTH
        else:
            print('no turn')

    # DEBUG TOOLS

    def print_all(self):
        print(f'name: {self.name}, exploded : {self.has_exploded}')
        print(f'pos: {self.position} - vel: {self.velocity} - acc: {self.acceleration} - dir: {self.direction}')