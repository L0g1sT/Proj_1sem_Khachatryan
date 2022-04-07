# В матрице элементы третьей строки заменить элементами из
# одномерного динамического массива соответствующей размерности.

import random

n = int(input('Введите количество столбцов: '))
m = int(input('Введите количество строк: '))

matr = [[random.randint(1, 10) for x in range(n)]for y in range(m)]
arr = [random.randint(1, 10) for i in range(m)]

print('\n','Массив:', '\n', arr, '\n')

print('Исходная матрица:')
for v in matr:
    print(v)

for i in range(m):
    for g in range(m):
        matr[2][g] = arr[i-g]

print()
print('Матрица после замены столбца:')
for v in matr:
    print(v)
