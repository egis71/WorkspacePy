zod = input("Įveskite žodį: ")

zd = list(zod)
z = zd[::-1]
atb = "".join(z)
print("Žodis atvirkščiai:", atb)

atb1 = ""
for r in zod:
    atb1 = r + atb1
print(atb1)

input()
