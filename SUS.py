import random
n = 0
a = []
b = []
f1 = open("file1.txt", "w", encoding="UTF-8")
for i in range(10):
    a.append(random.randint(0, 10))
    f1.write(str(a[i]))
    f1.write(" ")
f1.close()
f2 = open("file2.txt", "w", encoding="UTF-8")
for i in range(10):
    b.append(random.randint(-10, -1))
    f2.write(str(b[i]))
    f2.write(" ")
f2.close()
f1 = open("file1.txt")
i = f1.read()

f2 = open("file2.txt")
q = f2.read()

f3 = open("file3.txt", "w", encoding="UTF-8")
f3.write("Элементы первого и второго файлов: \n")
f3.write(i)
f3.write(q)
f3.write("\n")
f3.write("Количество Элементов первого и второго файлов: \n")
f3.write(str(len(a)))
f3.write("\n")
f3.write(str(len(b)))
f3.write("\n")
f3.write("Количество Элементов, общих для двух файлов:\n")
f3.write(str(len(a)+len(b)))
f3.write("\n")
f3.write("Количество четных элементов первого файла:\n")
for i in range(len(a)):
    if a[i] % 2 == 0:
        n += 1
f3.write(str(n))
n = 0
f3.write("\n")
f3.write("Количество нечетных элементов второго файла:\n")
for i in range(len(a)):
    if b[i] % 2 != 0:
        n += 1
f3.write(str(n))
f3.close()
n = 0
f1.close()
f2.close()
