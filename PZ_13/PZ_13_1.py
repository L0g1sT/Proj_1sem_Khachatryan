# Вариант №29
# Организовать и вывести последовательность на N произвольных целых
# элементов, сформировать новую последовательность куда поместить положительные
# чётные элементы, найти их сумму и среднее арифметическое

from random import randint

# Создаем список с Произвольными целыми числами
N = int(input("Введите N: "))
numbers = [randint(-99, 99) for i in range(N)]
length = len(numbers)
print(f'Старый список: {numbers}')

# Находим положительные чётные элементы и их количество
list_of_unique_numbers = []
for i in numbers:
    if i % 2 == 0 and i > 0:
        list_of_unique_numbers.append(i)
a = len(list_of_unique_numbers)

# Находим их сумму и среднее арифметическое
b = (sum(list_of_unique_numbers))
c = (sum(list_of_unique_numbers)/len(list_of_unique_numbers))

# Выводим
print(f'Новый список с чётными положительными: {list_of_unique_numbers}')
print(f'Их количество: {a}')
print(f'Сумма: {b}')
print(f'Среднее арифметическое: {int(c)}')


