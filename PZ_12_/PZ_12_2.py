# Дан целочисленный список A размера N. Переписать в новый целочисленный
# Список B того же размера вначале все элементы исходного списка
# С чётными номерами, а затем - с нечётными:A2,A4,A6...A1,A3,A5...
# Условный оператор не использовать.

from tkinter import *
import random


def mas(event):
    n = int(num1.get())
    a = []  # Создание списка
    t = 0
    b = []  # Создание списка

    while t < n:
        a.append(random.randint(0, 100))  # Создание элементов списка
        t += 1

    for i in range(2):
        while i % 2 == 0 and i < n:  # Сортировка списка (Сначала чётные индекс, затем нечётный)
            b.append(a[i])
            i += 2
        while i % 2 != 0 and i < n:
            b.append(a[i])
            i += 2

    text2 = Text(root, height=1, width=60, font='Arial 14', wrap=WORD)
    text2.place(x=25, y=80)
    text2.delete('1.0', END)
    text2.insert(1.0, str(a))

    text3 = Text(root, height=1, width=60, font='Arial 14', wrap=WORD)
    text3.place(x=25, y=145)
    text3.delete('1.0', END)
    text3.insert(1.0, str(b))


root = Tk()
root.title('PZ_12_2')
root.geometry('700x250')

label1 = Label(root, text="Введите размер списка A: ", font='Arial 12')
label1.place(x=25, y=20)

label2 = Label(root, text="Список A: ", font='Arial 12')
label2.place(x=25, y=55)

label3 = Label(root, text="Список B:", font='Arial 12')
label3.place(x=25, y=120)

num1 = Entry()
num1.place(x=275, y=25)

button1 = Button(text="Обработать")
button1.place(x=150, y=180)


button1.bind('<Button-1>', mas)

root.mainloop()
