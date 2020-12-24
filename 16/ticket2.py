instuff = open("ticket.in", "r")
instuff1 = instuff.read()
instuff2 = instuff1.split("\n\n")

# process fields
fields = {}
validfields = {}
for i in instuff2[0].split("\n"):
    i = i.split(":")
    key = i[0]
    val = []
    for j in i[1].split(" or "):
        r = []
        for k in j.split("-"):
            r.append(int(k))
        val.append(r)
    fields[key] = val
    validfields[key] = set(range(len(instuff2[2].split("\n")[1:][0].split(","))))


popindexes = set()

tickets = instuff2[2].split("\n")[1:]

for (c, i) in enumerate(tickets):
    for k in i.split(","):
        valid = False
        for j in fields.values():
            for l in j:
                if int(k) >= l[0] and int(k) <= l[1]:
                    valid = True
        if not valid:
            popindexes.add(c)

for index in sorted(popindexes, reverse=True):
    del tickets[index]
# validtickets = [i for j, i in enumerate(tickets) if j not in popindexes]
# validtickets.append(instuff2[1].split("\n")[1])
for i in tickets:
    for (c, j) in enumerate(i.split(",")):
        for (k, v) in fields.items():
            valid = False
            for l in v:
                if int(j) >= l[0] and int(j) <= l[1]:
                    valid = True
            if not valid:
                validfields[k].discard(c)


while max(map(len, validfields.values())) != 1:
    for (k, v) in validfields.items():
        if len(v) == 1:
            for w in validfields.values():
                if len(w) > 1:
                    w.discard(list(v)[0])


for (k, v) in validfields.items():
    print(k, ": ", *v)

result = 1
for (k, v) in validfields.items():
    if k.startswith("departure"):
        result *= int(instuff2[1].split("\n")[1].split(",")[list(v)[0]])

print(result)