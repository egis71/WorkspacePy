# -*- coding: utf-8 -*-
# TODO padaryti galimybe ivesti kartas


def gaunam_data(klaus):

    while True:
        born = input("Įveskite periodo "+klaus+" metus tarp 1944 ir 2023: ")
        if not born.isdigit():
            print("Reikia įvesti sveiką skaičių!")
            continue
        if int(born) < 1944 or int(born) > 2023:
            print("Galima įvesti metus tarp 1944 ir 2023 įskaitytinai!")
            continue
        born = int(born)
        return born


kartu_kiekis = int(input("Kelios bus kartos? : "))

kartos = {}
for i in range(kartu_kiekis):
    kart_name = input("Įveskite " + str(i+1) + "-os kartos pavadinimą: ")
    pr_data = gaunam_data("pradžios")
    gl_data = gaunam_data("pabaigos")
    kartos[kart_name] = [pr_data, gl_data]

print()
"""
kartos = {
    'lost': [1944, 1963],
    'X': [1964, 1983],
    'Y': [1984, 2003],
    'Z': [2004, 2023]
}
"""
# TODO padaryti rusiavima pagal datas
# kart = sorted(kartos.keys(), key=str.lower)
kart1 = sorted(kartos.values())
kart = []
for k in kart1:
    for i in kartos:
        if k == kartos[i]:
            kart.append(i)
            break

prad_data = gaunam_data("pradžios")
gal_data = gaunam_data("pabaigos")

# TODO rezultada pasidaryti ne string o duomenu struktura pvz zodynas
# {'karta': (data_nuo, data_iki), ...}
# s = str(prad_data) + " - " + str(gal_data) +\
#     ", rezultatas: " + str(prad_data) + " - "

# TODO pabandyti patobulinti palyginima pvz. kitaip lyginti ar naudoti funkcija
for k, v in kartos.items():
    if v[0] <= prad_data <= v[1]:
        prad_karta = k
    if v[0] <= gal_data <= v[1]:
        gal_karta = k

ats = {prad_karta: [prad_data]}

ind1 = kart.index(prad_karta)
ind2 = kart.index(gal_karta)

for i in range(ind1, ind2 + 1):
    if gal_data <= kartos[kart[i]][1]:
        ats[kart[i]].append(gal_data)
        # s += str(gal_data) + " " + str(kart[i]) + " karta"
    else:
        ats[kart[i]].append(kartos[kart[i]][1])
        ats[kart[i+1]] = [kartos[kart[i+1]][0]]
        # s += str(kartos[kart[i]][1]) + " " + str(kart[i]) + " karta, "
        # s += str(kartos[kart[i+1]][0]) + " - "

# print(s)
# TODO atspausdinti resultata is duomenu strukturos

print("{} - {}, rezultatas:".format(prad_data, gal_data))
for i, k in ats.items():
    print("{} - {} {} karta".format(k[0], k[1], i))
