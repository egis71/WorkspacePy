# -*- coding: utf-8 -*-
# import sys


def main(fname1, fname2):
    f1 = open(fname1)
    f2 = open(fname2)

    # Nuskaitome pirmas failų eilutes ir paverčiame sveik. skaičiais
    n1 = int(f1.readline())
    n2 = int(f2.readline())

    # Tikriname pradines pusfinalių dalyvių skaičių sąlygas
    if not 8 < n1 + n2 < 16 or not 2 <= n1 <= 8 or not 2 <= n2 <= 8:
        print("Bėgikų kiekiai neatitinka pradinių sąlygų.")
        f1.close()
        f2.close()
        return

    # Dedame pirmo pusfinalio dalyvius ir jų rezultatus į žodyną
    # pusf1 = {}
    # for l1 in f1:
    #     tmp = l1.split()
    #     pusf1[tmp[0] + " " + tmp[1]] = [int(tmp[2]) + int(tmp[3])/100]
    #
    # pusf2 = {}
    # for l2 in f2:
    #     tmp = l2.split()
    #     pusf2[tmp[0] + " " + tmp[1]] = [int(tmp[2]) + int(tmp[3])/100]

    # Kadangi kodas kartojasi, darom funkciją:
    def pusf_dict(file):
        pusf = {}
        for l in file:
            tmp = l.split()
            pusf[tmp[0] + " " + tmp[1]] = int(tmp[2]) + int(tmp[3])/100
        return pusf

    # Sudedame pusfinalių rezultatus į atskirus žodynus
    pusf1 = pusf_dict(f1)
    pusf2 = pusf_dict(f2)

    # Uždarome atidarytus failus
    f1.close()
    f2.close()

    # Tikriname, ar dalyvių skaičius lyginis
    # if len(pusf1) % 2 != 0:
    #     pusf1.pop(max(pusf1))
    #
    # if len(pusf2) % 2 != 0:
    #     pusf2.pop(max(pusf2))

    # Kodas vėl kartojasi, vadinasi reikia funkcijos,
    # kuri pašalins blogiausią (didžiausią) rezultatą
    def lyg_sk(pusf):
        if len(pusf) % 2 != 0:
            key_pasal = max(pusf, key=lambda x: pusf[x])
            del pusf[key_pasal]
        return pusf

    # Apdirbame pusfinalius pagal nurodytą sąlygą
    pusf1 = lyg_sk(pusf1)
    pusf2 = lyg_sk(pusf2)

    # Funkcija, kuri paliks po pusę geriausių bėgikų iš pusfinalių
    def pusf_geriausi(pusf):
        for i in range(int(len(pusf)/2)):
            key_pasal = max(pusf, key=lambda x: pusf[x])
            del pusf[key_pasal]
        return pusf

    # Ir gauname geriausius pusfinalių bėgikus
    pusf1g = pusf_geriausi(pusf1)
    pusf2g = pusf_geriausi(pusf2)

    print(pusf1g)
    print(pusf2g)


if __name__ == "__main__":
    # execute only if run as a script
    # print(sys.argv)

    # file_name = None
    # if len(sys.argv) == 2:
    #     file_name = sys.argv[1]
    # file_name1 = len(sys.argv) == 3 and sys.argv[1]
    # file_name2 = len(sys.argv) == 3 and sys.argv[2]

    # if file_name:
    #    main(file_name1, file_name2)
    # if len(sys.argv) == 3:
    file_name1 = 'pusf1.txt'
    file_name2 = 'pusf2.txt'
    main(file_name1, file_name2)
