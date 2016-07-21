# -*- coding: utf-8 -*-
print("Įveskite čiuožėjų kiekį ir teisėjų kiekį, atskirtus tarpu.")
print("Kiekiai turi būti sveiki skaičiai ")
print("Čiuožėjų kiekis nuo 1 iki 100, teisėjų - nuo 3 iki 100.")
while True:
    ciuoz_teisej = raw_input("Jūsų įvedimas: ")
    C, T = (ciuoz_teisej.strip().split())
    try:
        C, T = int(C), int(T)
    except Exception:
        print("Prašyčiau skaityti instrukciją! Sveiki skaičiai.")
        continue
    if (C not in range(1, 101)) or (T not in range(3, 101)):
        print("Kiekiai neatitinka sąlygų!")
        continue
    break
#    else:
#        break

print("Dabar turite įvesti {} čiuožėjų vardus,".format(C))
print("ir {} tesėjų įvertinimus nuo 0 iki 10 šalia vardo,\n"
      "atskiriant viską tarpeliu.".format(T))
print("Įvedę vieną vardą ir visų teisėjų įvertinimus, spauskite <Enter>:")

dalyviai = {}
vidurkiai = {}
for i in range(C):
    while True:
        ciuozejas = raw_input()
        print ciuozejas
        ciuozejas1 = ciuozejas.strip().split()
        print ciuozejas1

        if len(ciuozejas1) != T + 1:
            print("Jūsų įvedimas netinkamas. Bandykite dar ...")
            continue

        # dalyvio_vertinimas = dalyviai[ciuozejas1[0]]

        dalyvio_vertinimas = []

        try:
            for j in range(1, len(ciuozejas1)):
                dalyvio_vertinimas.append(float(ciuozejas1[j]))
        except Exception:
            print("Panašu, kad įvedėte ne skaičius. Kartokite.")
            continue


        max_pasalinimui = max(dalyvio_vertinimas)
        dalyvio_vertinimas.remove(max_pasalinimui)

        min_pasalinimui = min(dalyvio_vertinimas)
        dalyvio_vertinimas.remove(min_pasalinimui)

        vid = sum(dalyvio_vertinimas) / len(dalyvio_vertinimas)
        vidurkiai[ciuozejas1[0]] = vid

        break

# print(dalyviai)
# print(vidurkiai)
print(max(vidurkiai))
