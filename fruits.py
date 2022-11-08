
NAME_WIDTH = 16
PRICE_WIDTH = 8

fruits = ('Abacate', 'Melancia', 'Laranja', 'Banana', 'Limão', 'Uva')
prices = (7.54, 5.25, 3.10, 2.50, 5.90, 8.90)

print('-' * (NAME_WIDTH + PRICE_WIDTH))
print('%*s%*s' % (-NAME_WIDTH, 'ITEM', PRICE_WIDTH,'PREÇO'))
print('-' * (NAME_WIDTH + PRICE_WIDTH))

for i in range(len(fruits)):
    print('%-*s%*.2f' % (NAME_WIDTH, fruits[i], 
                         PRICE_WIDTH, prices[i]))

