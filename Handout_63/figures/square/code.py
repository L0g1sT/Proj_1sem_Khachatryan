def square_perimetr():
    print('1: Ввести свои стороны. 2: Использовать стандартные стороны.')
    n = int(input('Выберите число 1 или 2: '))
    while (n != 1) and (n != 2):
        try:
            print('Такого варианта нет')
            n = int(input('Выберите число 1 или 2: '))
        except ValueError:
            pass
    if n == 1:
        a = int(input('Введите сторну a: '))
    else:
        a = d_a
    p = a*4
    print('Периметр квадрата = ', p)


def square_area():
    print('1: Ввести свои стороны. 2: Использовать стандартные стороны.')
    n = int(input('Выберите число 1 или 2: '))
    while (n != 1) and (n != 2):
        try:
            print('Такого варианта нет')
            n = int(input('Выберите число 1 или 2: '))
        except ValueError:
            pass
    if n == 1:
        a = int(input('Введите сторну a: '))
    else:
        a = d_a
    s = a**2
    print("Площадь квадрата = ", s)


d_a = 15