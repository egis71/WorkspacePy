# -*- coding: utf-8 -*-
print("Įveskite čiuožėjų kiekį ir teisėjų kiekį, atskirtus tarpu.")
print("Kiekiai turi būti sveiki skaičiai ")
print("Čiuožėjų kiekis nuo 1 iki 100, teisėjų - nuo 3 iki 100.")
while True:
    ciuoz_teisej = input("Jūsų įvedimas: ")
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
        ciuozejas = input()
        ciuozejas1 = ciuozejas.strip().split()

        if len(ciuozejas1) != T + 1:
            print("Jūsų įvedimas netinkamas. Bandykite dar ...")
            continue

        # dalyviai[ciuozejas1[0]] = dalyviai[ciuozejas1[0]]

        dalyviai[ciuozejas1[0]] = []

        try:
            for j in range(1, len(ciuozejas1)):
                dalyviai[ciuozejas1[0]].append(float(ciuozejas1[j]))
        except Exception:
            print("Panašu, kad įvedėte ne skaičius. Kartokite.")
            continue


        max_pasalinimui = max(dalyviai[ciuozejas1[0]])
        dalyviai[ciuozejas1[0]].remove(max_pasalinimui)

        min_pasalinimui = min(dalyviai[ciuozejas1[0]])
        dalyviai[ciuozejas1[0]].remove(min_pasalinimui)

        vid = sum(dalyviai[ciuozejas1[0]]) / len(dalyviai[ciuozejas1[0]])
        vidurkiai[ciuozejas1[0]] = vid

        break

print(dalyviai)
print(vidurkiai)
print(max(vidurkiai.values()))
