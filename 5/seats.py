instuff = open("seats.in", "r")
instuff1 = instuff.readlines()

finalresult = 1

for i in instuff1:
    result = 0
    for p in range(7):
        if i[p] == "B":
            result += 2 ** (6 - p)
    result1 = 0
    for p in range(7, 10):
        if i[p] == "R":
            result1 += 2 ** (2 - (p - 7))
    finalresult = max(result1 + result * 8, finalresult)
print(finalresult)