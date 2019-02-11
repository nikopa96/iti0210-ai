class Cell:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.came_from = None

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_value(self):
        return self.value

    def set_came_from(self, came_from):
        self.came_from = came_from

    def get_came_from(self):
        return self.came_from

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.x == other.x \
               and self.y == other.y \
               and self.value == other.value
