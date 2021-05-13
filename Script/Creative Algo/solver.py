#!/usr/bin/python3

import more_itertools

x = 4
n = 12

r = [2**i for i in range(n)]

parts = more_itertools.set_partitions(r, k = x)

summed = []
for p in parts:
    o = set()
    for i in p:
        o.add(sum(i))
    summed.append(o)

print(len(summed))
