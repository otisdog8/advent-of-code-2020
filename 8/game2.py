instuff = open("game.in", "r")
instuff1 = instuff.readlines()


instructions = []
for i in instuff1:
    instructions.append(i.split(" "))
for i in range(len(instructions)):
    if instructions[i][0] == "nop":
        instructions[i][0] = "jmp"
    elif instructions[i][0] == "jmp":
        instructions[i][0] = "nop"
    instptr = 0
    solved = False
    acc = 0
    visited_instructions = set()
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
        if instptr == len(instructions):
            break
    if not solved:
        print(acc)
        break
    if instructions[i][0] == "nop":
        instructions[i][0] = "jmp"
    elif instructions[i][0] == "jmp":
        instructions[i][0] = "nop"
