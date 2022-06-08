# Вариант 29
# Составить генератор (yield), который преобразует все буквенные символы в строчные

# Функция, переведет символы строки из верхнего регистра в нижний.
def func_generator(ls):
    for i in ls:
        if type(i) == str:
            i = i.lower()
        yield i


lst = str(input("Введите буквенные символы: "))  # входные данные
q = []  # список, в который будет записан результат
generator = func_generator(lst)  # создаем генератор

# Добавляем элементы, которые возвращает yield, в список output
for j in generator:
    q.append(j)
res = ""
for i in q:
    res += i
print("Входные данные: ", lst)
print("Результат: ", res)  # вывод результата