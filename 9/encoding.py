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
        print(instuff1[i])
        break

    tempinstuff.append(instuff1[i])
    tempinstuff.pop(0)