# -*- coding: utf-8 -*-
import sys
# Importuojam reg. išraiškų modulį :)
import re

def main(file_name):
    # Sukuriame žodyną, kuriame bus laikomi žodžiai kaip raktai,
    # o jų reikšmės bus reikšmės, kiek kartų rastas tas žodis tekste.
    zod_counts = {}

    # Atidarome failą skaitymui
    with open(file_name, "r", encoding="utf-8-sig") as f:
        # Failą skaitome po eilutę
        for txt in f:

            # Sukuriame reg. išraiškos šabloną, kuris suras žodžius
            # \w atitinka [a-žA-Ž0-9_]
            p = re.compile(r"\w+")
            # Gauname visų žodžių eilutėje sarašą.
            zodziai = p.findall(txt)

            # Sudedame žodžius į žodyną
            for zodis in zodziai:
                # Jei žodžio dar nėra, sukuriame naują elementą
                if zodis.lower() not in zod_counts:
                    zod_counts[zodis.lower()] = 1
                # Jei žodis jau yra, pridedame vienetą prie jo reikšmės
                else:
                    zod_counts[zodis.lower()] += 1

    # Išvedame žodžius ir jų pasikartojimo kiekius, prieš tai
    # surikiavę mažėjančia tvarka pagal reikšmes
    for zod, sk in sorted(
                zod_counts.items(),
                key=lambda x: x[1],
                reverse=True):
            print(zod, sk)

if __name__ == "__main__":

    file_name = len(sys.argv) == 2 and sys.argv[1]

    if file_name:
        main(file_name)
