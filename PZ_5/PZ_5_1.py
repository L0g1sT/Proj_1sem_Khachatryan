# Составить функцию, которая напечатает сорок любых символов

def si(a, b):  # Создание функции
    while a >= 0:
        print(b)
        a -= 1


t = 40
s = input("Введите символ который хотите напечатать")
print(si(t, s))
