instuff = open("password.in", "r")
instuff1 = instuff.readlines()
instuff2 = []
for i in instuff1:
    stuff = []
    for s in i.split(" "):
        stuff.append(s)
    instuff2.append(stuff)

result = 0
for i in instuff2:
    start = int(i[0].split("-")[0])
    end = int(i[0].split("-")[1])
    letter = i[1].split(":")[0]
    som = 0
    for s in i[2]:
        if s == letter:
            som += 1
    if som >= start and som <= end:
        result += 1

print(result)