'''
Dada uma seqüência de N números reais, determinar 
os números que compõem a seqüência e o número de 
vezes que cada um deles ocorre na mesma.

Seqüência: 
-1.7, 3.0, 0.0, 1.5, 0.0, -1.7, 2.3, -1,7

Saída:
-1.7 ocorre 3 vezes
 3.0 ocorre 1 vez
 0.0 ocorre 2 vezes
 1.5 ocorre 1 vez
 2.3 ocorre 1 vez
'''

numbers = dict()

print('Informe uma sequência de números reais, um de cada vez, terminada por ENTER:')
while True:
    data = input('> ').strip()
    if not data:
        break
    
    data = float(data)
    # if data in numbers:
    #     numbers[data] = numbers[data] + 1
    # else:
    #     numbers[data] = 1
    numbers[data] = numbers.get(data, 0) + 1

for k,v in numbers.items():
    plural = 'es' if v > 1 else ''
    print('%5f ocorre %d vez%s' % (k, v, plural))
