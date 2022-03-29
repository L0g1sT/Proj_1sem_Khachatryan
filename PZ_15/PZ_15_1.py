# В матрице элементы последнего столбца заменить на -1
import random

i, j = 3, 3
print("Матрица: ")
matr = [[random.randint(1, 10) for x in range(i)]for y in range(j)]
for q in matr:
    print(q)
print("Элементы последнего столбца заменены на -1")
for i in range(j):
    matr[i][j-1] = [-1 for x in range(1)]
for q in matr:
    print(q)
