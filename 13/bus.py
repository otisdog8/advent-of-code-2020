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

found = False
while not found:
    for i in ttimes:
        if time % i == 0:
            print((time - itime) * i)
            found = True

    time += 1