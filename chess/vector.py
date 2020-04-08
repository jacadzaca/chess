import math


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def __eq__(self, other_vector):
        return (math.isclose(self.x, other_vector.x)
                and math.isclose(self.y, other_vector.y))

    def __hash__(self):
        '''the x and y components are squared and floored
        to avoid problems with floating point arithmetic
        this is not a perfect implementation, but good enough
        for the use case
        (we only hold vectors in hashtables, when they are unit length)'''
        return hash((math.floor(self.x**2), math.floor(self.y**2)))


def parse_vector(positon):
    '''vector can be parsed form a string like [digitdigit]
       Example: "02"
       Craetes a vector of Vector type'''
    if len(positon) != 2:
        raise ValueError('Can only create vectors from vectors of size 2')
    return Vector(int(positon[0]), int(positon[1]))
