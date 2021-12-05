# Описать функцию Swap(X,Y),меняющую содержимое переменных X и Y
# (X и Y-вещественные параметры, являющиеся одновременно входными и выходными)
# С её помощью для данных переменных A,B,C,D последовательно поменять
# Содержимое следующих пар: A и В, С и D, B и C и вывести новые значения
# A,B,C,D.

def Swap(X,Y): #Создание функции с формальными переменными
    Y,X = X,Y
    return X,Y

A = int(input("Введите число A: ")) #Создание переменных
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))
D = int(input("Введите число D: "))

print(Swap(A,B)) # Использование функции уже с фактическими переменными
A,B = Swap(A,B)

print(Swap(C,D))
C,D = Swap(C,D)

print(Swap(B,C))
B,C = Swap(B,C)

print(A,B,C,D)