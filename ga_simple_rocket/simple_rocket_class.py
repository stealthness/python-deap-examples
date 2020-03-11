"""
Simple Rocket is a rocket that can only move along the vertical axis
"""
from ga_rocket_example import config
import logging
LOGGING = False
logging.basicConfig(level=logging.DEBUG)


class SimpleRocket:

    def __init__(self, name) -> float:
        self.pos: float = 0.0
        self.vel: float = 0.0
        self.acc: float = 0.0
        self.name = name
        self.engine_force: float = 9.8
        self.engine_on = False
        self.has_failed = False
        self.has_landed = False
        self.logger = logging.getLogger(self.name)

    def __str__(self):
        return f'name:{self.name}, pos:{self.pos}, vel:{self.vel}, acc:{self.acc} \n landed:{self.has_landed}, crashed:{self.has_failed}'

    def update(self):
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
                logging.debug(f' -- pos:{self.pos:.3f}, vel:{self.vel:.3f}, acc:{self.acc:.3f}, engine on:{self.engine_on}')
            # return delta change
            return ds
        else:
            return 0.0

    def self_destruct(self):
        self.vel = 0.0
        self.acc = 0.0
        self.engine_on = False
        self.has_failed = True

    def complete_landing(self):
        self.vel = 0.0
        self.acc = 0.0
        self.engine_on = False
        self.has_landed = True

