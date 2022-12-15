
from math import pi as PI


class Cossine:

    def __init__(self, angle, count = None):
        if not isinstance(angle, (int, float)):
            raise TypeError('angle must be a numeric type.')

        if (count is not None) and (not isinstance(count, int)):
            raise TypeError('count must be an integer.')

        if count < 0:
            raise ValueError('count must be non negative')

        self.__angle = float(angle)
        self.__count = count
        self.__index = 0


    def __fat(n):
        f = 1
        for k in range(1, n + 1):
            f *= k
        return f


    def __iter__(self):
        return self


    def __next__(self):
        if self.is_finite() and (self.__index == self.__count):
            raise StopIteration()

        self.__index += 1

        signal = 1 if (self.__index % 2) else -1
        n = 2 * (self.__index - 1)
        term = signal * (self.__angle ** n) / Cossine.__fat(n) 
        return term


    def is_finite(self):
        return self.__count is not None


c1 = Cossine(PI / 2, 10)

c = 0.0
for t in c1:
    c += t

print('cos(PI) =', c)