
from math import sqrt
from point import Point

class Polygon:

    def __init__(self, arg):
        if isinstance(arg, (tuple, list)):
            self.__vertex = list()
            for p in arg:
                if isinstance(p, Point):
                    self.__vertex.append(p)
                else:
                    raise TypeError('Vertex is not a Point object')
        elif isinstance(arg, Polygon):
            self.__vertex = list(arg.__vertex)
        else:
            raise TypeError('Polygon needs a tuple or list as argument')
    
    # def __get_vertexes(self):
    #     return tuple(self.__vertex)

    def __repr__(self):
        # result = 'Polygon<'
        # for v in self.__vertex:
        #     result += str(v) + ', '
        # return result[:-2] + '>'
        return 'Polygon<' + ', '.join(map(str, self.__vertex)) + '>'


    vertexes = property(fget=lambda self: tuple(self.__vertex), doc='Polygon vertexes')

    def __eq__(self, pol):
        if len(self.__vertex) != len(pol.__vertex):
            return False

        for v in self.__vertex:
            if v not in pol.__vertex:
                return False
        return True
        # return set(self.__vertex) == set(pol.__vertex)

    def show(self, prompt=''):
        print(prompt, end='')
        print(self)

    def clone(self):
        return Polygon(self)

    def perimeter(self):
        p = 0.0
        vertex = self.__vertex
        for i in range(len(vertex) - 1):
            p += sqrt((vertex[i].x - vertex[i + 1].x)**2 + (vertex[i].y - vertex[i + 1].y)**2)
        return p 



a = Point(2,4)
b = Point(4,4)
c = Point(3,5)

t = Polygon([a, b, c,])

q = Polygon([
        Point(4, 2),
        Point(5, 2),
        Point(5, 3),
        Point(3, 3),
    ])

t2 = Polygon(t)

v = t.vertexes
print('vertex(t):', v)
print()
print('t:', t)

t.show()
t.show('T:')

print('p=',t.perimeter())
