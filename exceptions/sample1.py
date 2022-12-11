
try:
    a = int(input('Valor 1: '))
    b = int(input('Valor 2: '))
    print('------------')
    print(f'{a} / {b} = {a / b}')
    print('============')
except ValueError as e:
    print('Você deve digitar um número.')
    raise
# except ZeroDivisionError:
#     print('Não é possível dividir por zero')
else:
    print('Executei finally')
