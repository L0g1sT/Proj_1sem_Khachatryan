# Дан список A размера N и целое число K (1<K<N).Преобразовать список,
# увеличив каждый его элемент на исходное значение Элемента Ak

import random

N = int(input("Введите размер списка A: "))

A = []
t = 0
while t<N:
    A.append(random.randint(0,100))
    t+=1

print(A)
N = int((random.randint((0),(N-2))))

t = A.pop(N)
A.sort(reverse=True)
A.insert(N,t)
print(A)

for i in range(N):
    if A[N] <= A[i] and A[N] >= A[i+1]:
        A.insert(i,A[N])
        A.__delitem__(N+1)

print(A)