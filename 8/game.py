instuff = open("game.in", "r")
instuff1 = instuff.readlines()

visited_instructions = set()

instructions = []
for i in instuff1:
    instructions.append(i.split(" "))
instptr = 0
solved = False
acc = 0
while not solved:
    visited_instructions.add(instptr)
    if instructions[instptr][0] == "acc":
        acc += int(instructions[instptr][1])
        instptr += 1
    elif instructions[instptr][0] == "jmp":
        instptr += int(instructions[instptr][1])
    else:
        instptr += 1
    if instptr in visited_instructions:
        solved = True

print(acc)