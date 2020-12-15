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
        de = we - e
        dn = wn - n
        e += de * val
        n += dn * val
        we = de + e
        wn = dn + n
    elif select == "L":
        de = we - e
        dn = wn - n
        if val == 90:
            we -= de
            wn -= dn
            we -= dn
            wn += de
        elif val == 180:
            we -= de * 2
            wn -= dn * 2
        elif val == 270:
            we -= de
            wn -= dn
            we += dn
            wn -= de
    elif select == "R":
        de = we - e
        dn = wn - n
        if val == 90:
            we -= de
            wn -= dn
            we += dn
            wn -= de
        elif val == 180:
            we -= de * 2
            wn -= dn * 2
        elif val == 270:
            we -= de
            wn -= dn
            we -= dn
            wn += de
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