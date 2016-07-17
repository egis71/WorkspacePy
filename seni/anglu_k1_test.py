# -*- coding: utf-8 -*-

with open("anglu1000z1.txt", "rb") as f:
    for i, j in enumerate(f):
        a = f.readline()
        a1, a2 = a.split(sep=b";")
        a1 = str(a1, encoding='utf-8')
        a2 = str(a2, encoding='utf-8')
        print(i, str(a, encoding="UTF-8"), end="")
