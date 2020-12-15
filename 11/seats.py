from copy import deepcopy
import time

instuff = open("seats.in", "r")
instuff1 = instuff.readlines()

seats = []
row = []

for i in instuff1:
    for k in i:
        row.append(k)
    row.pop(len(row) - 1)
    seats.append(row)
    row = []


def derivative_check(x, y, dx, dy, arr):
    found = False
    result = 0
    while not found:
        if x + dx < 0 or x + dx >= len(arr) or y + dy < 0 or y + dy >= len(arr[0]):
            found = True
        else:
            x += dx
            y += dy
            if arr[x][y] == "L":
                found = True
            elif arr[x][y] == "#":
                found = True
                result = 1
    return result


result = False
while not result:
    for i in seats:
        s = ""
        for k in i[:-1]:
            s += k
    #    print(s)
    # print()

    prev = deepcopy(seats)
    cflag = False
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            rsum = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == 0 and l == 0:
                        continue
                    else:
                        rsum += derivative_check(i, j, k, l, prev)

            if rsum >= 5 and seats[i][j] == "#":
                cflag = True
                seats[i][j] = "L"
            elif rsum == 0 and seats[i][j] == "L":
                cflag = True
                seats[i][j] = "#"
    if not cflag:
        result = True
result = 0
for i in seats:
    for j in i:
        if j == "#":
            result += 1

print(result)