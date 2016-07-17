# print("sveiki")
# # Zodynas
# zodynas = {''}
# zodynas = dict()

kartos = {
    'lost': [1944, 1963],
    'X': [1964, 1983],
    'Y': [1984, 2003],
    'Z': [2004, 2023]
}
# kartos.items()
# [(karta, intervalas), ...]

# TODO padaryti pvz su list

# data = int(input('Iveskite data'))
data = input('Iveskite data:\n')
# konvertuojame i integer
# TODO padaryti isimciu valdyma
data = int(data)

# for k in kartos:
#     print(k, kartos[k])
#     intervalas = kartos[k]
#     print(k, intervalas)
# trumpiau

rezultatas = 'nerasta'
for karta, intervalas in kartos.items():
    # print(karta, intervalas)
    prad = intervalas[0]
    pab = intervalas[1]
    # pradzios data <= gimimo data <= pabaigos data
    # if prad <= data:
    #     if pab >= data:
    #         print('Radaom')
    if prad <= data and pab >= data:
        # print('Rezultatas:', karta)
        rezultatas = karta
        break

# rezultatas = karta
print('Rezultatas:', rezultatas)
