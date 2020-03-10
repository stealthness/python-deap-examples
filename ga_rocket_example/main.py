"""

"""
from graphics import *
from ga_rocket_example.config import WINDOW_SIZE


# create the GUI Grapthwin to add graphics to
win = GraphWin('Face', WINDOW_SIZE[0], WINDOW_SIZE[1])  # give title and dimensions

# End GUI

message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()