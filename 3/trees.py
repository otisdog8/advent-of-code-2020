instuff = open("trees.in", "r")
instuff1 = instuff.readlines()

runningres = 1

counter = 0
result = 0
for i in instuff1:
    if list(i)[counter % ((len(instuff1[0]) - 1))] == "#":
        result += 1
    counter += 1
runningres *= result
print(result)

counter = 0
result = 0
for i in instuff1:
    if list(i)[counter % (len(instuff1[0]) - 1)] == "#":
        result += 1
    counter += 3
runningres *= result
print(result)


counter = 0
result = 0
for i in instuff1:
    if list(i)[counter % (len(instuff1[0]) - 1)] == "#":
        result += 1
    counter += 5
runningres *= result
print(result)


counter = 0
result = 0
for i in instuff1:
    if list(i)[counter % (len(instuff1[0]) - 1)] == "#":
        result += 1
    counter += 7
runningres *= result
print(result)

counter = 0
result = 0
for i in range(len(instuff1) // 2 + 1):
    if list(instuff1[i * 2])[counter % (len(instuff1[0]) - 1)] == "#":
        result += 1
    counter += 1
runningres *= result
print(result)

print(runningres)