import re


p = re.compile(r"[8(863)]+[0-9]+[0-9]+[0-9]+[-]+[0-9]+[0-9]+[-]+[0-9]+[0-9]")
with open('hotline_1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print(p.findall(text))
print(len(p.findall(text)))
