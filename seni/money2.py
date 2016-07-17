def banknotes_counts(banknotes_gets, suma):
    """Function to calculate banknotes"""

    banknotes = sorted(banknotes_gets.keys(), reverse=True)
    for banknote in banknotes:
        if suma >= banknote:
            banknotes_gets[banknote] = suma // banknote
            suma = suma % banknote
    # ??return banknotes_gets


banknotes_get = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0}

suma = int(input("Kiek pinigų imsite?: "))

kupiuros = banknotes_counts(banknotes_get, suma)

print("-" * 70)
if suma < 5:
    print("Jums nepasisekė. Negausite nieko...")
else:
    viso = 0
    for k in sorted(kupiuros.keys(), reverse=True):
        if kupiuros[k] > 0:
            print("Kupiūrų su nominalu '{}' gausite "
                  "{} vnt.".format(k, kupiuros[k]))
            viso += k * kupiuros[k]
    print("Viso gauta suma:", viso)
print("-" * 70)
