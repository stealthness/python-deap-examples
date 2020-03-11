import numpy as np
from graphics import *
from ga_rocket_example.config import *
from ga_rocket_example.functions import get_rocket_shape
from ga_rocket_example.config import WINDOW_SIZE
from ga_rocket_example.rocket_class import Rocket
from ga_simple_rocket.functions import get_ground_and_sky_limit

# create the GUI Grapthwin to add graphics to
win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])  # give title and dimensions

rocket = Rocket('r0')
rocket.main_engine_on = True

start_point = Point(win.getWidth()//2, win.getHeight() - WIN_ADJUST)

shape = get_rocket_shape(start_point, 0)
shape.draw(win)

t = 0
while t < MAX_TIME_INTERVALS:
    dx, dy = rocket.update([0, 1, 0])
    shape.move(dx, dy)
    t += 1

get_ground_and_sky_limit(win)

message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()