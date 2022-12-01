
class Rational:
  
    def __init__(self, num, den = None):
        self.__num, self.__den = self.__validate_params(num, den)


    def __validate_params(self, num, den):
        if isinstance(num, int) and isinstance(den, int):
            if den == 0:
                raise ValueError('Denominator cannot be 0')
        elif isinstance(num, int) and (den is None):
            den = 1
        elif isinstance(num, Rational) and (den is None):
            num, den = num.__num, num.__den
        elif isinstance(num, str) and (den is None):
            num, den = tuple(map(int, num.split('/')))
            num, den = self.__validate_params(num, den)
        else:
            TypeError('Invalid argument type')

        if den < 0:
            num = -num
            den = -den

        return (num, den)


    def __validate_operand(self, n):
        if not isinstance(n, (int, Rational)):
            raise TypeError(f'Invalid operando type: {n}')

        return Rational(n, 1) if isinstance(n, int) else n


    def __repr__(self):
        return f'Rational({self.__num},{self.__den})'


    def __str__(self):
        return f'{self.__num}/{self.__den}'


    def __hash__(self):
        return hash((self.__num, self.__den))


    def __add__(self, r):
        r = self.__validate_operand(r)
        return Rational(
                    self.__num * r.__den + r.__num * self.__den,
                    self.__den * r.__den 
               )


    def __radd__(self, r):
        return self.__add__(r)


    def __sub__(self, r):
        r = self.__validate_operand(r)
        return Rational(
                    self.__num * r.__den - r.__num * self.__den,
                    self.__den * r.__den 
               )


    def __rsub(self, r):
        return self.__sub__(r)


    def __mul__(self, r):
        r = self.__validate_operand(r)
        return Rational(
                    self.__num * r.__num,
                    self.__den * r.__den 
               )

    def __rmul__(self, r):
        return self.__mul__(r)


    def __truediv__(self, r):
        r = self.__validate_operand(r)
        return Rational(
                    self.__num * r.__den,
                    self.__den * r.__num 
               )

    def __rtruediv__(self, r):
        r = self.__validate_operand(r)
        return r.__truediv__(self)


    def __pos__(self):
        return self


    def __neg__(self):
        return Rational(-self.__num, self.__den)


    def __cmp(self, r):
        r = self.__validate_operand(r)
        result = (self.__num / self.__den) - (r.__num / r.__den)
        return 0 if result == 0 else (-1 if result < 0 else 1)


    def __eq__(self, r):
        return self.__cmp(r) == 0


    def __ne__(self, r):
        return self.__cmp(r) != 0


    def __gt__(self, r):
        return self.__cmp(r) > 0


    def __lt__(self, r):
        return self.__cmp(r) < 0


    def __ge__(self, r):
        return self.__cmp(r) >= 0


    def __le__(self, r):
        return self.__cmp(r) <= 0


    def reduce(self):
        div = 2
        num, den = self.__num, self.__den
        
        while div <= min(abs(num), abs(den)):
            if (num % div == 0) and (den % div == 0):
                num = num // div
                den = den // div
            else:
                div += 1

        self.__num = num
        self.__den = den
