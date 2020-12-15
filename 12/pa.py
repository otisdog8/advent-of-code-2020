import math

instuff = open("pa.in", "r")
instuff1 = instuff.readlines()


direction = 90
e = 0
n = 0
we = 10
wn = 1

for i in instuff1:
    select = i[:1]
    val = int(i[1:])
    if select == "F":
        e += math.sin(direction * math.pi / 180) * val
        n -= math.cos(direction * math.pi / 180) * val
    elif select == "L":
        direction += val
        direction = direction % 360
    elif select == "R":
        direction -= val
        direction = direction % 360
    elif select == "N":
        wn += val
    elif select == "S":
        wn -= val
    elif select == "E":
        we += val
    elif select == "W":
        we -= val
    print((e), " ", (n))

print(math.fabs(e) + math.fabs(n))