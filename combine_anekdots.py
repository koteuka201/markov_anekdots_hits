# -*- coding: utf-8 -*-

with open("anekdots_slice2.txt", "r", encoding="cp1251") as f:
    lines = f.readlines()

anekdots = []
current = ""

for line in lines:
    line = line.strip()
    if line:  # строка не пуста€
        if current:
            current += " " + line
        else:
            current = line
    else:  # пуста€ строка Ч конец анекдота
        if current:
            anekdots.append(current)
            current = ""

if current:
    anekdots.append(current)

with open("anekdots_one_line.txt", "w", encoding="utf-8") as f:
    for a in anekdots:
        f.write(a + "\n")
