# Выполнить сортировку словаря d = {'a': 1, 'b': 2, 'c': 3}
d = {'a': 1, 'b': 2, 'c': 3}
d1 = {}
k = sorted(d, reverse=True)
for i in range(len(d)):
    d1.update({k[i]: 3-i})
print(d1)

