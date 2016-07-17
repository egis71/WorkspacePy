# -*- coding: utf-8 -*-


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

# TODO padaryti įvedimą iš failo
kartos = {}
with open('band.txt', 'r') as f:
    for line in f:
        a, b, c = line.strip().split(sep=',')
        kartos[a] = [int(b), int(c)]

# TODO padaryti rusiavima pagal datas

kart1 = sorted(kartos.items(), key=lambda x: x[1])

kart = []
for k in kart1:
    kart.append(k[0])

prad_data = gaunam_data("pradžios")
gal_data = gaunam_data("pabaigos")

# TODO rezultada pasidaryti ne string o duomenu struktura pvz zodynas


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
    else:
        ats[kart[i]].append(kartos[kart[i]][1])
        ats[kart[i+1]] = [kartos[kart[i+1]][0]]

# TODO atspausdinti resultata is duomenu strukturos

print("{} - {}, rezultatas:".format(prad_data, gal_data))
for i, k in sorted(ats.items(), key=lambda x: x[1]):
    print("{} - {} {} karta".format(k[0], k[1], i))
