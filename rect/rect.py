
class Rect:

    def __init__(self, width, height=None, name=''):
        if not isinstance(name, str):
            raise TypeError('Argument name must be a string')
        self.__name = name

        if isinstance(width, (int, float)):
            self.__width = width
            if isinstance(height, (int, float)):
              self.__heigth = height
            elif height is None:
                self.__heigth = width
            else:
                TypeError('Invalid argument type')
        elif isinstance(width, Rect) and (height is None):
            r = width
            self.__width = r.__width
            self.__heigth = r.__heigth
        else:
            raise TypeError('Invalid argument types')

    def __repr__(self):
        name = self.__name if self.__name else 'Rect'
        return f'{name}({self.__width},{self.__heigth})' 

    def __cmp(self, r):
        return self.area() - r.area()

    def __eq__(self, r):
        return self.__cmp(r) == 0

    def __ne__(self, r):
        return self.__cmp(r) != 0

    def __lt__(self, r):
        return self.__cmp(r) < 0

    def __le__(self, r):
        return self.__cmp(r) <= 0

    def __gt__(self, r):
        return self.__cmp(r) > 0

    def __ge__(self, r):
        return self.__cmp(r) >= 0

    def area(self):
        return self.__width * self.__heigth

    def perimeter(self):
        return 2*self.__width + 2*self.__heigth




r1 = Rect(10,5,'R1')
r2 = Rect(8,12)
r3 = Rect(2,25,'R3')
