kartos = {
    'lost': [1944, 1963],
    'X': [1964, 1983],
    'Y': [1984, 2003],
    'Z': [2004, 2023]
}
kart = sorted(kartos.keys(), key=str.lower)


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

prad_data = gaunam_data("pradžios")
gal_data = gaunam_data("pabaigos")

s = str(prad_data) + " - " + str(gal_data) +\
    ", rezultatas " + str(prad_data) + " - "

for k in kartos:
    if kartos[k][0] <= prad_data <= kartos[k][1]:
        prad_karta = k
    if kartos[k][0] <= gal_data <= kartos[k][1]:
        gal_karta = k

ind1 = kart.index(prad_karta)
ind2 = kart.index(gal_karta)

for i in range(ind1, ind2 + 1):
    if gal_data <= kartos[prad_karta][1]:
        s += str(gal_data) + " " + str(prad_karta) + " karta"
    else:
        s += str(kartos[prad_karta][1]) + " " + str(prad_karta) + " karta, "


print(s)
