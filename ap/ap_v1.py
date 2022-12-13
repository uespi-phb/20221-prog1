
class AP:

    def __init__(self, first, diff, n = -1):
        self.__first = first
        self.__diff = diff
        self.__count = n


    def __repr__(self):
        return f'AP({self.__first},{self.__diff},{self.__count})'


    def __validate_index(self, index):
        if isinstance(index, int):
            if self.is_finite() and ((index <= 0) or (index > self.__count)):
                raise IndexError(f'Invalid index: {index}')
        else:
            raise TypeError(f'Invalid index type: {start}')


    def __getitem__(self, slc):
        if isinstance(slc, int):
            return self.term_at(slc)
        elif isinstance(slc, slice):
            elems = list()
            start = slc.start if slc.start is not None else 1
            stop  = slc.stop if slc.stop is not None else self.__count

            self.__validate_index(start)
            self.__validate_index(stop)

            if start > stop:
                raise IndexError(f'Invalid index range')

            elems = list()
            elem = self.term_at(start)

            for _ in range(stop - start + 1):
                elems.append(elem)
                elem += self.__diff

            return elems
        else:
            raise TypeError(f'Invalid index type: {slc}')


    first = property(lambda self: self.__first)
    diff = property(lambda self: self.__diff)
    count = property(lambda self: self.__count)


    def is_finite(self):
        return self.__count >= 0


    def is_infinite(self):
        return self.__count < 0


    def term_at(self, index):
        if index <= 0:
            raise IndexError(f'Invalid index: {index}')

        if self.is_finite() and (index > self.__count):
            raise IndexError(f'Index out of range: {index}')

        return self.__first + (index - 1) * self.__diff


    def sum(self, n = -1):
        if self.is_finite():
            if n > self.__count:
                raise IndexError(f'Number of elements out of range: {n}')
            if n < 0:
                n = self.__count
        else:
            if n < 0:
                raise ValueError(f'Invalid number of elements: {n}')

        return n*(self.__first + self.term_at(n)) / 2



ap1 = AP(1,1,10)
ap2 = AP(-5,2)

print(ap1)
print('a1:', ap1.first)
print('r :', ap1.diff)
print('n :', ap1.count)

print(ap2)
print('a1:', ap2.first)
print('r :', ap2.diff)
print('n :', ap2.count)

print('ap1[5]:', ap1[5])
print('ap1[3:6]:', ap1[3:6])
print('ap1[:6]:', ap1[:6])
print('ap1[3:]:', ap1[3:])
print('ap1[:]:', ap1[:])
