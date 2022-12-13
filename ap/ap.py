
class ArithmeticProgression:

    def __init__(self, first, diff, count = None):
        if not isinstance(first, (int, float)):
            raise TypeError(f'First term must be of a numeric type: {first}')

        if not isinstance(diff, (int, float)):
            raise TypeError(f'Difference term must be of a numeric type: {diff}')

        self.__first = first
        self.__diff = diff
        self.__count = count
        self.__n = 0


    def __repr__(self):
        return f'ArithmeticProgression({self.__first},{self.__diff})'
    

    def __iter__(self):
        return self


    def __next__(self):
        if (self.__count is not None) and (self.__n == self.__count):
            raise StopIteration()

        self.__n += 1
        return self.get_term(self.__n)


    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')

        return self.get_term(index)


    def get_term(self, index):
        if (index < 1) or (self.__count is not None) and (index > self.__count):
            raise IndexError('Index out of range')

        return self.__first + (index - 1)*self.__diff

    first = property(lambda self: self.__first)
    count = property(lambda self: self.__count)


evens = ArithmeticProgression(0, 2)
digs = ArithmeticProgression(0, 1, 10)


for d in digs:
    print(d, end=' ')
print()

print('a1 =', digs.first)
print('a5 =', digs.get_term(5))
#print('a5 =', digs.get_term(-5))
#print('a50 =', digs.get_term(50))
print('a[7] =', digs[7])
