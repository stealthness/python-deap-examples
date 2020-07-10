"""
Simple Rocket is a rocket that can only move along the vertical axis
"""
from ga_rocket_example import config
import logging
LOGGING = False


class SimpleRocket:

    def __init__(self, name, engine_force=20, engine_on=False, pos=0.0, vel=0.0, acc=-9.8) -> float:
        self.name = name
        self.pos: float = pos
        self.vel: float = vel
        self.acc: float = acc
        self.engine_force: float = engine_force
        self.engine_on = engine_on
        self.has_failed = False
        self.has_landed = False

    def __str__(self):
        return f'name:{self.name}, pos:{self.pos}, vel:{self.vel}, acc:{self.acc} \n landed:{self.has_landed}, crashed:{self.has_failed}'

    def update(self):
        """
        Updates the the rockets pos, vel, acc
        :return:
        """
        if not self.has_landed and not self.has_failed:
            delta_time = 1.0 / float(config.TIME_INTERVALS)
            # update acc
            if self.engine_on:
                self.acc = config.GRAVITY_1d + self.engine_force
            else:
                self.acc = config.GRAVITY_1d

            # update velocity
            self.vel += self.acc * delta_time

            # update pos
            ds = (self.vel - self.acc * delta_time/2) * delta_time
            self.pos += ds

            # logging
            if LOGGING:
                print(f' -- pos:{self.pos:.3f}, vel:{self.vel:.3f}, acc:{self.acc:.3f}, engine on:{self.engine_on}')
            # return delta change
            return ds
        else:
            return 0.0

    def self_destruct(self):
        """
        destroys the rocket, has_failed set to True
        :return:
        """
        self.vel = 0.0
        self.acc = 0.0
        self.engine_on = False
        self.has_failed = True

    def complete_landing(self):
        """
        successful landing, has_landed set to True
        :return:
        """
        self.vel = 0.0
        self.acc = 0.0
        self.engine_on = False
        self.has_landed = True

