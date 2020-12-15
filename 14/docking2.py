instuff = open("docking.in", "r")
instuff1 = instuff.readlines()

mem = {}

lines = []
for i in instuff1:
    if i.startswith("mask"):
        lines.append(i.split(" ")[-1][:-1])
    else:
        lines.append((int(i.split("[")[1].split("]")[0]), int(i.split(" ")[-1])))

mask = ""

for i in lines:
    if len(i) == 2:
        binary = list(f"{i[0]:36b}")
        for j in range(len(binary)):
            if binary[j] in [" ", "0"]:
                binary[j] = 0
            else:
                binary[j] = 1
        fc = 0
        fa = []
        for j in range(len(binary)):
            if mask[j] == "X":
                binary[j] = "0"
                fc += 1
                fa.append(j)
            elif mask[j] == "1":
                binary[j] = 1

        for j in range(2 ** fc):
            m = bin(j)[2:]
            while len(m) != fc:
                m = "0" + m
            for k in range(len(m)):
                binary[fa[k]] = int(m[k])
            binary1 = ""
            for j in binary:
                binary1 += str(j)
            mem[int(binary1, 2)] = i[1]
    else:
        mask = i
result = 0
for i in mem.values():
    result += i
print(result)