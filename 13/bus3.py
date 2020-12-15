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


found = False
check = 1
while not found:
    for i in ttimes[1:]:
        if check % i != 0:
            break
    else:
        print(check)


from math import gcd

lcm = cycles[0]
for i in cycles[1:]:
    lcm = lcm * i // gcd(lcm, i)

print(lcm)
