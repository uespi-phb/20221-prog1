
# Construir uma matrix identidade N x N

n = 3
m = list()
for i in range(n):
    m.append([0] * n)
    m[i][i] = 1
