instuff = open("recitation.in", "r")
instuff1 = instuff.readlines()

numbers = []

for i in instuff1[0].split(","):
    numbers.append(int(i))

while len(numbers) < 30000001:
    if numbers[-1] not in numbers[:-1]:
        numbers.append(0)
    else:
        for i in reversed(range(len(numbers) - 1)):
            if numbers[i] == numbers[-1]:
                numbers.append(len(numbers) - i - 1)
                break
    if len(numbers) % 1000000 == 0:
        print(len(numbers))

print(numbers[30000000 - 1])
