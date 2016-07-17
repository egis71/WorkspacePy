# -*- coding: utf-8 -*-

txt = input("Įveskite tekstą: \n")

tvark_simb = "(),.?! " # Kokie simboliai bus apdirbami
skyr_znkl = ",.?! " # Skyrybos ženklai
txt_new = "" # Bus saugomas sutvarkytas tekstas

for i, t in enumerate(txt): # Gaudom raidžių indeksus ir pačias raides
    # Susikuriame kintamąjį, kuris turės savyje sekančią raidę,
    # patikrindami, ar tai ne paskutinis simbolis.
    if i == len(txt) - 1:
        txt_new += t
        break
    else:
        sek_simb = txt[i+1]
    # Kol simbolis nėra tvarkomų sąraše, dedame jį į naują tekstą.
    if t not in tvark_simb:
        txt_new += t
    # Jei randam tarpelį...
    elif t == " ":
        if sek_simb != ")" and sek_simb not in skyr_znkl and txt[i-1] != "(":
            txt_new += t
    # Jei radom skyrybos ženklą...
    elif t in skyr_znkl:
        if sek_simb == " ":
            txt_new += t
        else:
            txt_new += t + " "
    # Ir t.t. :)
    elif t == "(" and i != 0:
        if txt[i-1] == " ":
            txt_new += t
        else:
            txt_new += " " + t
    elif t == ")":
        if sek_simb in skyr_znkl or sek_simb == " ":
            txt_new += t
        else:
            txt_new += t + " "

print(txt_new)
