# Даны числа х, у, x1, y1, х2, у2. Проверить истинность высказывания:
# «Точка с координатами (х, у) лежит внутри прямоугольника,
# левая верхняя вершина которого имеет координаты (х1, у1),
# правая нижняя — (х2, у2), а стороны параллельны координатным осям».

x = input('Введите число x: ')
while type(x) != float:    # Обработка исключений
    try:
        x = float(x)
    except ValueError:
        print("Введено не число!")
        x = input("Введите число x:  ")
y = input('Введите число y: ')
while type(y) != float:    # Обработка исключений
    try:
        y = float(y)
    except ValueError:
        print("Введено не число!")
        y = input("Введите число y:  ")
x1 = input('Введите число x1: ')
while type(x1) != float:    # Обработка исключений
    try:
        x1 = float(x1)
    except ValueError:
        print("Введено не число!")
        x1 = input("Введите число x1:  ")
y1 = input('Введите число y1: ')
while type(y1) != float:    # Обработка исключений
    try:
        y1 = float(y1)
    except ValueError:
        print("Введено не число!")
        y1 = input("Введите число y1:  ")
x2 = input('Введите число x2: ')
while type(x2) != float:    # Обработка исключений
    try:
        x2 = float(x2)
    except ValueError:
        print("Введено не число!")
        x2 = input("Введите число x2:  ")
y2 = input('Введите число y2: ')
while type(y2) != float:    # Обработка исключений
    try:
        y2 = float(y2)
    except ValueError:
        print("Введено не число!")
        y2 = input("Введите число y2: ")

if (x2 > x > x1) and (y2 < y < y1) and (x1 < x2) and (y1 > y2) :
    print("Высказывание истинное!")
else:
    print("Высказываение ложное!")
