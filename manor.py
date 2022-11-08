
a = int(input('1o. Número: '))
b = int(input('2o. Número: '))

# Solution #1
if a > b:
    print(a,'é maior que',b)
else:
    if a < b:
        print(b,'é maior que',a)
    else:
        print(a,'é igual a',b)

# Solution #2
if a > b:
    print(a,'é maior que',b)
elif a < b:
    print(b,'é maior que',a)
else:
    print(a,'é igual a',b)

# Solution #3
if max(a,b) == a:
    print(a,'é maior que',b)
elif max(a,b) == b:
    print(b,'é maior que',a)
else:
    print(a,'é igual a',b)

