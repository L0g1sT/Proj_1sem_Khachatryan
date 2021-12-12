# Выполнить сортировку словаря d = {'a': 1, 'b': 2, 'c': 3}
d = {'a': 1, 'b': 2, 'c': 3}
k = sorted(d, reverse=True)
for i in range(len(d)):
    d.update({k[i]: 1+i})
print(d)
# Я не совсем понял условие. Надеюсь, что решил правильно
