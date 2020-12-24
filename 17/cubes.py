from collections import defaultdict
from copy import deepcopy

instuff = open("cubes.in", "r")
instuff1 = instuff.read()

d = defaultdict(
    lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))
)

dbw1 = -1
dbw2 = 1
dbx1 = -1
dbx2 = 1
dby1 = -1
dby2 = len(instuff1.split("\n")) + 1
for (c1, i) in enumerate(instuff1.split("\n")):
    for (c2, j) in enumerate(i):
        d[0][0][c1][c2] = True if j == "#" else False
dbz1 = -1
dbz2 = len(instuff1.split("\n")[0]) + 1

for i in range(6):
    calcdict = deepcopy(d)
    for w in range(dbw1 - 1, dbw2 + 2):
        for x in range(dbx1 - 1, dbx2 + 2):
            for y in range(dby1 - 1, dby2 + 2):
                for z in range(dbz1 - 1, dbz2 + 2):
                    neighbors = 0
                    for w1 in range(-1, 2):
                        for x1 in range(-1, 2):
                            for y1 in range(-1, 2):
                                for z1 in range(-1, 2):
                                    if calcdict[w + w1][x + x1][y + y1][
                                        z + z1
                                    ] and not (
                                        x1 == 0 and y1 == 0 and z1 == 0 and w1 == 0
                                    ):
                                        neighbors += 1
                    if neighbors == 3:
                        d[w][x][y][z] = True
                    elif neighbors == 2 and calcdict[w][x][y][z]:
                        pass
                    else:
                        d[w][x][y][z] = False
                    if i == 0:
                        pass
                        # print("detected", neighbors, "at", x, y, z)
    for w in range(dbw1 - 1, dbw2 + 2):
        for x in range(dbx1 - 1, dbx2 + 2):
            for y in range(dby1 - 1, dby2 + 2):
                for z in range(dbz1 - 1, dbz2 + 2):
                    if d[w][x][y][z]:
                        dbw1 = min(dbw1, w - 1)
                        dbw2 = max(dbw2, w + 1)
                        dbx1 = min(dbx1, x - 1)
                        dbx2 = max(dbx2, x + 1)
                        dby1 = min(dby1, y - 1)
                        dby2 = max(dby2, y + 1)
                        dbz1 = min(dbz1, z - 1)
                        dbz2 = max(dbz2, z + 1)
    if False:
        for w in range(dbw1 - 1, dbw2 + 2):
            for x in range(dbx1, dbx2 + 1):
                print("X:", x, " \n")
                for y in range(dby1, dby2 + 1):
                    for z in range(dbz1, dbz2 + 1):
                        pass
                        print("#" if d[w][x][y][z] else ".", end="")
                    print()
cubes = 0
for w in range(dbw1 - 1, dbw2 + 2):
    for x in range(dbx1 - 1, dbx2 + 2):
        for y in range(dby1 - 1, dby2 + 2):
            for z in range(dbz1 - 1, dbz2 + 2):
                if d[w][x][y][z]:
                    cubes += 1
print(cubes)