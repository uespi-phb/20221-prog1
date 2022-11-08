
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
    # def __str__(self):
    #     return '(%f,%f)' % (self.__x, self.__y)
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
        return (self.x == p.x) and (self.y == p.y)


p1 = Point()
p2 = Point(3,8)
p3 = Point(p2)

print('p1 =', p1)
print('p2 =', p2)
print('p3 =', p3)
print()
print('(p2.x, p2.y) = (', p2.x, ',', p2.y, ')')
print('p1 == p2: ', p1.equal(p2))
print('p2 == p3: ', p2.equal(p3))

