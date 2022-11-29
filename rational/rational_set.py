
from rational import Rational


class RationalSet:

    def __init__(self):
        self.__data = set()


    def __repr__(self):
        return '{%s}' % (', '.join(map(str, self.__data)))


    def __str__(self):
        return self.__repr__()


    def __validate_set(self, s):
        if not isinstance(s, RationalSet):
            raise TypeError('Union is supported only for RationalSet')


    def __validate_element(self, e):
        if not isinstance(e, (int, Rational)):
            raise TypeError('Element must be int or Rational')
        return Rational(e, 1) if isinstance(e, int) else e


    def __contains__(self, e):
        e = self.__validate_element(e)
        return e in self.__data


    def __add__(self, s):
        self.__validate_set(s)

        u = RationalSet()
        u.__data = self.__data.union(s.__data)
        return u


    def __mul__(self, s):
        self.__validate_set(s)

        i = RationalSet()
        i.__data = self.__data.intersection(s.__data)
        return i


    def __sub__(self, s):
        self.__validate_set(s)

        d = RationalSet()
        d.__data = self.__data.difference(s.__data)
        return d


    def __eq__(self, s):
        self.__validate_set(s)
        return self.__data == s.__data


    def __ne__(self, s):
        self.__validate_set(s)
        return self.__data != s.__data


    def __gt__(self, s):
        self.__validate_set(s)
        return self.__data > s.__data

    def __ge__(self, s):
        self.__validate_set(s)
        return self.__data >= s.__data


    def __lt__(self, s):
        self.__validate_set(s)
        return self.__data < s.__data


    def __le__(self, s):
        self.__validate_set(s)
        return self.__data <= s.__data


    def add(self, e):
        e = self.__validate_element(e)
        self.__data.add(e)


    def discard(self, e):
        e = self.__validate_element(e)
        self.__data.discard(e)

