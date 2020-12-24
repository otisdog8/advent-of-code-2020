instuff = open("recitation.in", "r")
instuff1 = instuff.readlines()

numbers = []
nums = set()
last = {}

for (k, i) in enumerate(instuff1[0].split(",")):
    numbers.append(int(i))
    if k != len(instuff1[0].split(",")) - 1:
        last[int(i)] = k
        nums.add(int(i))
lnum = numbers[-1]
bruh = len(numbers)
while bruh < 30000000:
    if lnum not in nums:
        nums.add(lnum)
        last[lnum] = bruh - 1
        bruh += 1
        lnum = 0
    else:
        val = bruh - last[lnum] - 1
        last[lnum] = bruh - 1
        numbers.append(val)
        lnum = val
        bruh += 1

print(lnum)
