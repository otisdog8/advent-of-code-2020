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
        binary = list(f"{i[1]:36b}")
        for j in range(len(binary)):
            if binary[j] in [" ", "0"]:
                binary[j] = 0
            else:
                binary[j] = 1
        for j in range(len(binary)):
            if mask[j] == "X":
                pass
            else:
                binary[j] = int(mask[j])
        binary1 = ""
        for j in binary:
            binary1 += str(j)
        mem[i[0]] = int(binary1, 2)
    else:
        mask = i
result = 0
for i in mem.values():
    result += i
print(result)