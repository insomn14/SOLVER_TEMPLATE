from pwn import *
import time

r = remote('challenges.ctfd.io', 30264)

import random, time
s = time.time()

print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
n = [x for x in range(20)]

for x in range(len(n)):
    r.recvline()
    r.recv()
    r.send("r\n")
    n[x] = int(r.recvline().decode("utf-8")[:-1])

print(n)
print("Starting bruteforce")

found = False
for x in range(200):
    random.seed(round((s + x / 1000) / 100, 5))
    for y in range(len(n)):
        if random.randint(1, 100000000) != n[y]:
            continue
        if y + 1 == len(n):
            print("Found x:", x)
            found = True
            break
    if found:
        break

if not found:
    print("Failed finding offset!")

random.seed(round((s + x / 1000) / 100, 5))
for x in range(len(n)):
    random.randint(1, 100000000)
print("Initialized seed with:", s, x)

print(r.recvline())
print(r.recv())
r.send("g\n")
print(r.recvline())
print(r.recvline())
print(r.recvline())
r.send("%d\n" % random.randint(1, 100000000))
print(r.recvline())
print(r.recvline())
r.send("%d\n" % random.randint(1, 100000000))
print(r.recvline())
print(r.recvline().decode("utf-8"))
