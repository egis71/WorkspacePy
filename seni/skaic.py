# -*- coding: utf-8 -*-

print("Skaičiai nuo 1 iki 100, kurie iš abiejų pusių yra vienodi.")
for i in range(1, 100):
    if i < 10:
        print(i)
    else:
        if i == i%10*10 + i//10:
            print(i)
