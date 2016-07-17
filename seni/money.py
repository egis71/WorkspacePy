def bancnots_counts(bancnots, bancnots_get, suma):
    for bancnot in bancnots:
        if suma >= bancnot:
            bancnots_get[bancnot] = suma // bancnot
            suma = suma % bancnot
    return bancnots_get


bancnots = [100, 50, 20, 10, 5]
bancnots_get = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0}
suma = int(input("Kiek pinigų imsit?: "))


kupiuros = bancnots_counts(bancnots, bancnots_get, suma)

for k in sorted(kupiuros.keys()):
    if kupiuros[k] > 0:
        print("Kupiūrų su nominalu {} gausite {} vnt.".format(k, kupiuros[k]))
