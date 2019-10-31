class Vector():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def difference(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __eq__(self, other_vector):
        return self.x == other_vector.x and self.y == other_vector.y


def parse_vector(positon):
    '''vector can be parsed form a string like [digitdigit]
       Example: "02"
       Craetes a vector of Vector type'''
    return Vector(int(positon[0]), int(positon[1]))
