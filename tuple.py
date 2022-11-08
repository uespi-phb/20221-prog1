
n = int(input('Informe N: '))

l = list()
for k in range(n):
    l.append(k)
t = tuple(l)
print(t)

# Pythonic Way
t = tuple(range(n))
print(t)