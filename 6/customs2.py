instuff = open("customs.in", "r")
instuff1 = instuff.readlines()


customs = []
custom = []

for i in instuff1:
    if len(i) == 1:
        customs.append(custom)
        custom = []

    else:
        custom.append(i)

count = 0

for c in customs:
    result = set()
    for i in c:
        for j in i[:-1]:
            if j not in result:
                result.add(j)
    total = 0
    for i in result:
        for j in c:
            if i not in j:
                break
        else:
            total += 1
    count += total

print(count)