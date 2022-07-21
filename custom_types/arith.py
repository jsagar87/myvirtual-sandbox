from math import hypot


class Vector(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __abs__(self):
        return hypot(self._x, self._y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar):
        return Vector(self._x * scalar, self._y * scalar)

    def __str__(self):
        return "x={0} and y={1}".format(self._x, self._y)

