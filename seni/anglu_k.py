# -*- coding: utf-8 -*-

ad = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
with open("anglu1000z.txt", "rb") as f:
    for i in range(10):
        a = f.readline()
        a1, a2 = a.strip().split(sep=b";")
        a1 = str(a1, encoding='utf-8')
        a2 = str(a2, encoding='utf-8')
        ad[0].append([a1, a2])
with open("anglu1000zj.txt", "ab") as f1:
    f1.write(ad)
# print(str(a, encoding="UTF-8"), end="")
