
import random

N = int(input("Введите размер списка A: "))
A = [] #Создание списка
t = 0
B = [] #Создание списка

while t < N:
    A.append(random.randint(-100, 100))  # Создание элементов списка
    t += 1
print(A)
for i in range(N-1):
    if i % 2 == 0:
        B.append(A[i])
print(B)
