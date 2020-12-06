instuff = open("seats.in", "r")
instuff1 = instuff.readlines()

ids = []

for i in instuff1:
    result = 0
    for p in range(7):
        if i[p] == "B":
            result += 2 ** (6 - p)
    result1 = 0
    for p in range(7, 10):
        if i[p] == "R":
            result1 += 2 ** (2 - (p - 7))
    ids.append(result * 8 + result1)

ids.sort()

prev = 0
for i in ids:
    if i - prev == 2:
        print(i - 1)
    else:
        prev = i