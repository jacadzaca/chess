import math


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

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @y.setter
    def y(self, new_y):
        self._y = new_y

    def direction(self):
        '''calcualte unit length vector'''
        return self / self.length()

    def __truediv__(self, nubmer):
        return Vector(self.x / nubmer, self.y / nubmer)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __sub__(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __add__(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def completly_equal(self, other_vector):
        '''checks if the value and direction of the vector is the same '''
        return math.isclose(self.x, other_vector.x) and math.isclose(self.y, other_vector.y)

    def __eq__(self, other_vector):
        '''checks only if the values are equal, neglects the direction '''
        return math.isclose(abs(self.x), abs(other_vector.x)) and math.isclose(abs(self.y), abs(other_vector.y))


def parse_vector(positon):
    '''vector can be parsed form a string like [digitdigit]
       Example: "02"
       Craetes a vector of Vector type'''
    if len(positon) != 2:
        raise ValueError('Can only create vectors from vectors of size 2')
    return Vector(int(positon[0]), int(positon[1]))
