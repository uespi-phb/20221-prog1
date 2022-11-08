
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

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.__x = float(x)
        else:
            raise TypeError('Invalid argument type')

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self.__y = float(y)
        else:
            raise TypeError('Invalid argument type')


p1 = Point()
p2 = Point(3,8)
p3 = Point(p2)

print('(p2.x, p2.y) = (', p2.get_x(), ',', p2.get_y(), ')')
p2.x = 'fdjfdh'
print('(p2.x, p2.y) = (', p2.x, ',', p2.y, ')')
