import numpy as np
from graphics import *
from ga_rocket_example.functions import get_rocket_shape
from ga_rocket_example.config import WINDOW_SIZE

# create the GUI Grapthwin to add graphics to
win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])  # give title and dimensions

r0 = get_rocket_shape(Point(50, 100), 0)
r1 = get_rocket_shape(Point(50, 150), 30)
r2 = get_rocket_shape(Point(50, 200), 90)
r3 = get_rocket_shape(Point(50, 250), 150)
r4 = get_rocket_shape(Point(50, 300), 180)
r5 = get_rocket_shape(Point(50, 350), 270)
r6 = get_rocket_shape(Point(50, 400), 300)

r0.draw(win)
r1.draw(win)
r2.draw(win)
r3.draw(win)
r4.draw(win)
r5.draw(win)
r6.draw(win)

message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()