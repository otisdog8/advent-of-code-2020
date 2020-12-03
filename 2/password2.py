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
    if (i[2][start - 1] == letter) ^ (i[2][end - 1] == letter):
        result += 1

print(result)