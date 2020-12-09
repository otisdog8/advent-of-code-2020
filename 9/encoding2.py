instuff = open("encoding.in", "r")
instuff1 = instuff.readlines()

preamble = 25

instuff2 = []
for i in instuff1:
    instuff2.append(int(i))
instuff1 = instuff2

tempinstuff = []
for i in range(preamble):
    tempinstuff.append(instuff1[i])

for i in range(preamble, len(instuff1)):
    result = False
    for j in tempinstuff:
        for k in tempinstuff:
            if j + k == instuff1[i] and j != k:
                result = True
    if not result:
        result = instuff1[i]
        break

    tempinstuff.append(instuff1[i])
    tempinstuff.pop(0)


for i in range(len(instuff1) - 1):
    for j in range(i + 1, len(instuff1) - 1):
        sumi = 0
        for k in range(i, j):
            sumi += instuff1[k]
        if sumi == result:
            mini = instuff1[i]
            maxi = instuff1[i]
            for k in range(i, j):
                mini = min(mini, instuff1[k])
                maxi = max(maxi, instuff1[k])
            print(mini + maxi)
        elif sumi > result:
            break