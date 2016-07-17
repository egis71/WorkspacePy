# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

with open("anglu1000z2.txt", "rb") as f:
    for a in f:

        a1, a2 = a.split(sep=b";")
        a1 = str(a1, encoding='utf-8')
        a2 = str(a2, encoding='utf-8')
        c.execute("INSERT INTO zodynas (zod_angl, zod_lt,"
                  " skyrius) VALUES (?, ?, ?)", (a1, a2, 0))
        conn.commit()

conn.close()

# print(str(a, encoding="UTF-8"), end="")
