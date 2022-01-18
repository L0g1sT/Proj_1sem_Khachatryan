import random
n = 0
f1 = open("file1.txt", "w", encoding="UTF-8")
for i in range(10):
    y = random.randint(-10, 10)
    if y < 0:
        n += 1
    f1.write(str(y))
    f1.write(" ")
f1.close()
y = 0
f2 = open("file2.txt", "w", encoding="UTF-8")
for i in range(10):
    y = random.randint(-10, 10)
    if y < 0:
        n += 1
    f2.write(str(y))
    f2.write(" ")
f2.close()
f1 = open("file1.txt")
i = f1.read()

f2 = open("file2.txt")
q = f2.read()

f3 = open("file3.txt", "w", encoding="UTF-8")
f3.write("Элементы первого и второго файлов: \n")
f3.write(i)
f3.write("\n")
f3.write(q)
f3.write("\n")
f3.write("Количество Элементов первого и второго файлов: \n")
f3.write()
f1.close()
f2.close()
