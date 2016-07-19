# TODO Parašyti programą, kuri užrašo gautą tekstą tel. mygtukų paspaudimais

klav = {
    "ABC":2, "CDF":3, "GHI":4, "JKL":5, 'MNO':6,
    "PQRS":7, "TUV":8, "WXYZ":9, " ":0
}

tekstas = input("Įveskite tekstą:\n")

seka = ""
for raid in tekstas:

    raid = raid.upper()

    for k, v in klav.items():
        if raid in k:
            seka += str(v) * (k.index(raid)+1)

print("Spaudykite tel. skaičius:",seka)

