import itertools

instuff = open("adapter.in", "r")
instuff1 = instuff.readlines()

instuff1 = map(int, instuff1)

instuff1 = list(instuff1)

instuff1.append(0)

instuff1.sort()

instuff1.append(max(instuff1) + 3)

diffs = []
diff = []
fresult = 1
for i in range(len(instuff1) - 1):
    diff1 = instuff1[i + 1] - instuff1[i]

    if diff1 == 3 and len(diff) != 0:
        if len(diff) > 2:
            diffs.append(diff)
        diff = []
    elif len(diff) > 0:
        diff.append(instuff1[i + 1])
    elif diff1 < 3:
        diff.append(instuff1[i])
        diff.append(instuff1[i + 1])


for i in diffs:
    print(i)
    if len(i) == 3:
        result = 2
    elif len(i) == 4:
        result = 4
    elif len(i) == 5:
        result = 7
    fresult *= result


print(fresult)