
from random import randint

n = int(input('Введите размер списка:'))
lst = [randint(0, 50) for i in range(n)]
ls = []

n -= 1
print(lst)

hlp = round((lst[1] + lst[0]) / 2, 1)
ls.insert(0, hlp)

for i in range(n+1):
    if i < n and i != 0:
        hlp = round((lst[i]+lst[i-1]+lst[i+1])/3, 1)
        ls.insert(i+1, hlp)

hlp = round((lst[n-1] + lst[n]) / 2, 1)
ls.insert(n, hlp)
print(ls)
