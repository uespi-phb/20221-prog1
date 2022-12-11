"""
ATENÇÃO O CÓDIGO DESTE ARQUIVO SERÁ USADO PARA TESTAR
SUA IMPLEMENTAÇÃO.

NÃO ALTERE AS FUNÇÕES NELE EXISTENTES.

SEU CÓDIGO DEVERÁ SE ADAPTAR ÀS CHAMADAS
AQUI CODIFICADOS.
"""

# Os imports poderão ser alterados para se
# adaptarem ao seu projeto
from individual import Individual


# Imprime uma linha
def lprint(len=80):
    print('-'*len)


# Impressão tabulada
def tprint(text, tabs=[]):
    data = text.split('\t')

    tabs_count = len(tabs)
    for t in range(len(data)):
        text = data[t]
        if t < tabs_count:
            text = '%*s' % (-tabs[t], text)
        print(text, end='')
    print()


def main():
    # Sequência de possíveis genótipos
    genotypes = ('AA','Ai','BB','Bi','AB','ii')

    # Cria individuos para teste
    individuals = list()

    tabs = (8, 9, 5, 12)
    tprint('NOME\tGENÓTIPO\tTIPO\tAGLUTININAS\tAGLUTINÓGENOS', tabs)
    for genotype in genotypes:
        indiv = Individual(genotype)
        tprint(f'{indiv.name}\t{indiv.genotype}\t{indiv.blood_type}\t{indiv.agglutinins}\t\t{indiv.agglutinogens}', tabs)

        individuals.append(indiv)
    print()

    tabs = (18, 11, 15, 15)
    tprint('CRUZAMENTO\t\tPOSSÍVEIS\tPOSSÍVEIS', tabs)
    tprint('NOMES\tGENOTIPOS\tGENÓTIPOS\tTIPOS', tabs)
    for i1 in range(len(individuals)):
        for i2 in range(i1,len(individuals)):

            indiv1 = individuals[i1]
            indiv2 = individuals[i2]

            cross_types = ','.join(indiv1.offsprings_blood_types(indiv2))
            cross_genotypes = ','.join(indiv1.offsprings_genotypes(indiv2))

            tprint(f'{indiv1.name} x {indiv2.name}\t{indiv1.genotype} x {indiv2.genotype}\t{cross_genotypes}\t{cross_types}', tabs)
    print()

    tabs = (18, 10, 8, 8)
    tprint('NOMES\tTIPOS\tDOAR\tRECEBER', tabs)

    sample = tuple(filter(lambda i: i.genotype in ('Ai','Bi','AB','ii'), individuals))

    for indiv1 in sample:
        for indiv2 in sample:

            can_donate = 'Y' if indiv1.can_donate(indiv2) else 'N'
            can_receive = 'Y' if indiv1.can_receive(indiv2) else 'N'

            tprint(f'{indiv1.name} x {indiv2.name}\t{indiv1.blood_type} -> {indiv2.blood_type}\t{can_donate}\t{can_receive}', tabs)
    print()

if __name__ == '__main__':
    main()
