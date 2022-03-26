# В исходном текстовом файле (hotline1.txt) найти все номера телефонов,
# шаблону 8(000)000-00-00. Посчитать количество полученных
# элементов. После фразы «Горячая линия» добавить фразу «Министерства
# образования Ростовской области», выполнив манипуляции в новом файле.
import re

p = re.compile(r"[8(863)]+[0-9]+[0-9]+[0-9]+[-]+[0-9]+[0-9]+[-]+[0-9]+[0-9]")
with open('hotline_1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print(p.findall(text))
print(len(p.findall(text)))
f1 = open("hotline_2.txt", "w", encoding="UTF-8")
with open("hotline_2.txt", "w", encoding="UTF-8") as file:
    text = re.sub("«Горячая линия»", "«Министерства образования Ростовской области»", text)
    f1.write(text)
