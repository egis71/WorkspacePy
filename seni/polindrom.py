# -*- coding: utf-8 -*-

print("Įveskite skaičių, iki kiek ieškoti polindrominių skaičių:")
riba = int(input())
print("Skaičiai nuo 1 iki {}, kurie iš abiejų pusių yra vienodi: "
      .format(riba))
k = 0
for i in range(1, riba+1):
    iatb = str(i)
    iatb1 = iatb[::-1]
    if iatb == iatb1:
        # print(iatb1, end=' ')
        print("{:>5}".format(iatb), end=' ')
        k += 1
        if k % 10 == 0:
            print()
