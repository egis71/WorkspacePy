# -*- coding: utf-8 -*-
kartos = {
    'lost': [1944, 1963],
    'X': [1964, 1983],
    'Y': [1984, 2003],
    'Z': [2004, 2023]
}
ats = False
while ats == False:
    born = raw_input("Įveskite metus tarp 1944 ir 2023: ")
    if not born.isdigit():
        print("Reikia įvesti sveiką skaičių!")
        continue
    if int(born) < 1944 or int(born) > 2023:
        print("Galima įvesti metus tarp 1944 ir 2023 įskaitytinai!")
        continue
    born = int(born)
    ats = True
# for k in sorted(kartos, key = str.lower):
#     print("Karta: {}. Periodas nuo {} m. iki {} "
#           "m.".format(k, kartos[k][0], kartos[k][1]))

for k, v in kartos.items():
    if v[0] <= born <= v[1]:
        # print(str(born) + ", rezultatas:", k, "karta.")
        print("{}, rezultatas: {} karta.".format(born, k))
