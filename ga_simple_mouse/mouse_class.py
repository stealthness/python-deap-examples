""""
This is the simple mouse class
"""


class IntMouse:

    def __init__(self, name, default_movement=1, **kwargs):
        self.name = name
        self.x = 0
        self.y = 0
        self.default_movement = default_movement
        self.commands = []

    def __str__(self):
        return f'name:{self.name}\npos:{self.get_pos()}\ncommands:{self.commands}'

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        if self.n > len(self.commands):
            raise StopIteration
        return self.commands[self.n-1]

    def get_pos(self) -> tuple:
        """
        Returns the the mouse position as a tuple
        :return:
        """
        return self.x, self.y

    def move(self, command: str):
        if command == 'right':
            self.x += self.default_movement
        if command == 'left':
            self.x -= self.default_movement
        if command == 'up':
            self.y += self.default_movement
        if command == 'down':
            self.y -= self.default_movement


