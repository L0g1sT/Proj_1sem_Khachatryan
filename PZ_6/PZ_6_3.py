# Дан список размера N. Осуществить сдвиг элементов списка в  право
# на одну позицию (при этом A1 перейдёт в A2,A2-в A3,AN-1 - в AN,
# А исходное значение последнего элемента будет потеряно).
# Первый элемент полученного списка положить равным 0.

import random

n = int(input("Введите размер списка A: "))
a = []  # Создание списка
t = 1

while t < n:
    a.append(random.randint(0, 100))  # Создание элементов списка
    t += 1
print(a)

a.insert(0, 0)  # Добавление 0 в начало списка
a.__delitem__(n - 1)  # Удаление последнего элемента списка
print(a)
