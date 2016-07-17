# -*- coding: utf-8 -*-
# Programa, kuri tikrina, ar trikampis statusis

print("Įveskite trikampio kraštinių ilgius:")
krastines = []
for i in range(1, 4):
    a = input("{}-os kraštinės ilgis: ".format(i))
    krastines.append(a)
a, b, c = krastines
a = float(a)
b = float(b)
c = float(c)

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Trikampis status")
elif a == b == c:
    print("Trikampis lygiakraštis")
else:
    print("Trikampis įvairiakraštis.")
