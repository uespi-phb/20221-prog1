
class BloodType:

    alleles = {
        'A': 1, 
        'B': 1,
        'i': 0
    }

    def __init__(self, symbol):
        if symbol not in BloodType.alleles:
            raise ValueError(f'Invalid blood type symbol. Valid symbols are: {",".join(BloodType.alleles.keys())}.')
        self.__symbol = symbol
        self.__domain = BloodType.alleles[symbol]

    def __repr__(self):
        return f'BloodType({self.__symbol})'

    def __str__(self):
        return self.__symbol

    def __validate_operand(self, operand):
        if not isinstance(operand, BloodType):
            raise TypeError('Operand must be an instance of BloodType')

    def __cmp_domain(self, operand):
        self.__validate_operand(operand)
        return self.__domain - operand.__domain

    def __gt__(self, operand):
        return self.__cmp_domain(operand) > 0

    def __lt__(self, operand):
        return self.__cmp_domain(operand) < 0

    def __cmp_symbol(self, operand):
        self.__validate_operand(operand)
        return self.__symbol == operand.__symbol

    def __eq__(self, operand):
        return self.__cmp_symbol(operand)

    def __ne__(self, operand):
        return not self.__cmp_symbol(operand)


a = BloodType('A')
b = BloodType('B')
i = BloodType('i')
