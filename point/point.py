import math
#from math import sqrt

class Point:
    def __init__(self, x = None, y = None):
        if (x is None) and (y is None):
            self.__x = 0.0
            self.__y = 0.0
        elif isinstance(x, (int, float)) and \
           isinstance(y, (int, float)):
            self.__x = float(x)
            self.__y = float(y)
        elif isinstance(x, Point) and (y is None):
            p = x
            self.__x = p.__x
            self.__y = p.__y
        else:
            raise TypeError('Invalid argument type')
    #
    def __repr__(self):
        return 'Point(%f,%f)' % (self.__x, self.__y)
    #
    def __str__(self):
        return '(%f,%f)' % (self.__x, self.__y)
    #
    def __get_coord(self, attr):
        return getattr(self, '_Point%s' % (attr))
    #
    def __set_coord(self, attr, value):
        if isinstance(value, (int, float)):
            setattr(self, '_Point%s' % (attr), float(value))
        else:
            raise TypeError('Invalid argument type')
    #
    x = property(lambda self: self.__get_coord('__x'),
                 lambda self, value: self.__set_coord('__x', value)
        )
    y = property(lambda self: self.__get_coord('__y'), 
                 lambda self, value: self.__set_coord('__y', value)
        )
    #
    def equal(self, p):
        return (self.__x == p.__x) and (self.__y == p.__y)
    #
    def dist(self, p):
        return math.sqrt((self.__x - p.__x)**2 + (self.__y - p.__y)**2)
    #
    def clone(self):
        return Point(self.__x, self.__y)

