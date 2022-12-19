
indiv_counter = 0

class Individual:

    __individual_counter = 0

    def __init__(self, genotype, name=None):
        self.__genotype = Individual.validate_genotype(genotype)
        self.__name = Individual.__generate_name(name)


    def validate_genotype(genotype):
        if not isinstance(genotype, str):
            raise TypeError('Genotype must be a string')

        if genotype not in ('AA', 'Ai', 'BB', 'Bi', 'AB', 'ii'):
            raise ValueError('Invalid genotype')

        return genotype


    def __generate_name(name):
        if name is None:
            Individual.__individual_counter += 1
            name = f'Indiv{Individual.__individual_counter}'

        return name


    def __repr__(self):
        return f'Individual({self.__genotype},{self.__name})'


    def __str__(self):
        return f'{self.__name}({self.__genotype})'


    name = property(
        lambda self: self.__name,
        doc='Get individual name'
    )

    genotype = property(
        lambda self: self.__genotype,
        doc='Get genotype string'
    )

    blood_type = property(

    )


i1 = Individual('AB', 'Maria')
i2 = Individual('Bi', 'Pedro')
i3 = Individual('ii')
i4 = Individual('AA')
