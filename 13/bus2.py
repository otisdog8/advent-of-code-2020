instuff = open("bus.in", "r")
instuff1 = instuff.readlines()

time = int(instuff1[0][:-1])
itime = time
times = instuff1[1][:-1].split(",")

ttimes = []

for i in times:
    if i == "x":
        pass
    else:
        ttimes.append(int(i))

cycles = []

for i in ttimes[1:]:
    cycletest = set()
    cycletest.add(0)
    total = ttimes[0]
    found = False
    while not found:
        total += ttimes[0]
        total = total % i
        if total not in cycletest:
            cycletest.add(total)
        else:
            found = True
    print(len(cycletest))
    cycles.append(len(cycletest))

from math import gcd

lcm = cycles[0]
for i in cycles[1:]:
    lcm = lcm * i // gcd(lcm, i)

print(lcm)
