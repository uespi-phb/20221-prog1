#
# Escreva um programa que verifique se um número inteiro
# N é prinmo
#

print('### VERIFICA SE UN NÚMERO N É PRIMO ###')

n = int(input('Digite N: '))

# if n > 0:
#     prime = True
#     for d in range(2, n):
#         if n % d == 0:
#             prime = False
#             break
# else:
#     prime = False

prime = n > 0
for d in range(2, n):
    if n % d == 0:
        prime = False
        break

if prime:
    print(n, 'é primo')
else:
    print(n, 'não é primo')
