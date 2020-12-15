instuff = open("adapter.in", "r")
instuff1 = instuff.readlines()

instuff1 = map(int, instuff1)

instuff1.append(0)

instuff1.sort()

instuff1.append(max(instuff1) + 3)

diffs = [0, 0, 0]

for i in range(len(instuff) - 1):
    diff = instuff[i + 1] - instuff[i]
    diffs[diff - 1] += 1

print(diffs[0] * diffs[2])