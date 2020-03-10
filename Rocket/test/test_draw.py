import numpy as np
from graphics import *
from ge_rocket_example.functions import get_rocket_shape
from ge_rocket_example.config import WINDOW_SIZE

# create the GUI Grapthwin to add graphics to
win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])  # give title and dimensions

r0 = get_rocket_shape(np.array([0, 100]), 0)
r1 = get_rocket_shape(np.array([0, 150]), 1)
r2 = get_rocket_shape(np.array([0, 200]), np.pi/2)
r3 = get_rocket_shape(np.array([0, 250]), 2)
r4 = get_rocket_shape(np.array([0, 300]), np.pi)
r5 = get_rocket_shape(np.array([0, 350]), 3*np.pi/2)
r6 = get_rocket_shape(np.array([0, 400]), 2*np.pi-0.1)

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