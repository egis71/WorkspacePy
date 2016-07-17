# -*- coding: utf-8 -*-
import sys
import itertools
import re


def main(file_name):
    # Atidarome failą ir nuskaitome asmens kodą
    f = open(file_name)
    asm_kod = f.readline().strip()
    f.close()

    # Naudodami reg. išraiškas, patikriname, ar
    # perduotas asmens kodas atitinka užrašymo taisykles
    p = re.compile(r"^[1-6][0-9]{2}[0-1][0-9][0-3][0-9][0-9]{4}$")
    if not p.match(asm_kod):
        print("Kodas užrašytas su klaidomis!")
        return

    # Tolesniam patikrinimui pasiverčiame asmens kodą į skaičių sąrašą
    asm_kod_list = list(asm_kod)
    # Pašaliname paskutinį elementą ir išsaugome jį tolesniam patikrinimui
    kontrol_sk = asm_kod_list.pop()

    # Analizuojame asm. kodą
    # Nustatome, kokiame amžiuje asmuo gimė ir kokia jo lytis
    sk0 = int(asm_kod[0])
    if sk0 < 3:
        print("Asmuo gimė XIX amžiuje.", end=" ")
        # Išsisaugome amžių kaip skaičių vėlesniam naudojimui
        amz = 19
    elif sk0 < 5:
        print("Asmuo gimė XX amžiuje.", end=" ")
        amz = 20
    else:
        print("Asmuo gimė XXI amžiuje.", end=" ")
        amz = 21

    if sk0 % 2 == 0:
        print("Asmuo yra moteris.")
    else:
        print("Asmuo yra vyras.")

    # Gražesniam datos išvedimui pasidarome mėnesių žodinį sąrašą.
    men = ["sausio", "vasario", "kovo",
           "balandžio", "gegužės", "birželio",
           "liepos", "rugpjūčio", "rugsėjo",
           "spalio", "lapkričio", "gruodžio"]

    # Formuojame asmens gimimo datą
    print("Asmens gimimo data:", end=" ")
    gim_data = str(amz-1) + asm_kod[1:3] + " m. " +\
        men[int(asm_kod[3:5])-1] + " men. " + asm_kod[5:7] + " d."
    print(gim_data)

    print("Tą dieną gimusių asmenų registre eilės numeris yra:", end=" ")
    print(int(asm_kod[7:10]))

    # Funkcijos, kurios bus naudojamos map() funkcijose (skaičių sandauga)
    def sand(sk1, sk2):
        sk1 = int(sk1)
        return sk1 * sk2

    def sand1(sk1, sk2):
        sk1 = int(sk1)
        if sk2 > 9:
            sk2 -= 9
        return sk1 * sk2

    # Pagal gautą formulę gauname  skaičių sąrašus ir juos susumuojame
    s1 = list(map(sand, asm_kod_list, itertools.cycle(range(1, 10))))
    sum1 = sum(s1)
    s2 = list(map(sand1, asm_kod_list, itertools.cycle(range(3, 12))))
    sum2 = sum(s2)

    # Pagal duotas sąlygas randame, koks turi būti kontrolinis skaičius
    if sum1 % 11 != 10:
        ksk = sum1 % 11
    elif sum2 % 11 != 10:
        ksk = sum2 % 11
    else:
        ksk = 0

    # Išvedimui panaudojame dar vieną if sąlygos mutaciją :)
    print("Kontrolinis skaičius praėjo patikrą? :",
          "Ne" if ksk != int(kontrol_sk) else "Taip")


if __name__ == "__main__":
    # execute only if run as a script
    # print(sys.argv)

    # file_name = None
    # if len(sys.argv) == 2:
    #     file_name = sys.argv[1]
    file_name = len(sys.argv) == 2 and sys.argv[1]

    if file_name:
        main(file_name)
