
# Escreva um programa que imprima os 
# N primeiros números naturais ímpares

print('*** Exibe os N primeiros números inteiros ímpares ***\n')

# Solution #1
n = int(input('Qtde de números: '))

m = n
k = 1
while m > 0:
    print(k, end='')
    if m > 1:
        print(',', end='')
    else:
        print()

    k += 2       # k = k + 2
    m -= 1       # n = n - 1

# Solution #2
print(str(list(range(1, 2*n + 1, 2)))[1:-1])
