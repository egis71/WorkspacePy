# -*- coding: utf-8 -*-

kartos = {}
with open('band.txt', 'r') as f:
    for line in f:
        a, b, c = line.strip().split(sep=',')
        kartos[a] = [int(b), int(c)]

kart1 = sorted(kartos, key=kartos.get)
print(kart1)

kart = []
for k in kart1:
    kart.append(k[0])
print(kart)
