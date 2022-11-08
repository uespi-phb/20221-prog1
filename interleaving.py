
l1 = [10,20,30]
l2 = [11,22,33,44,55]

r = list()
i1 = i2 = 0
while (i1 < len(l1)) or (i2 < len(l2)):
    if i1 < len(l1):
        r.append(l1[i1])
        i1 += 1
    if i2 < len(l2):
        r.append(l2[i2])
        i2 += 1

print(l1)
print(l2)
print(r)