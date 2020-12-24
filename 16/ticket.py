instuff = open("ticket.in", "r")
instuff1 = instuff.read()
instuff2 = instuff1.split("\n\n")

# process fields
fields = {}
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

result = 0
for i in instuff2[2].split("\n")[1:]:
    for k in i.split(","):
        valid = False
        for j in fields.values():
            for l in j:
                if int(k) >= l[0] and int(k) <= l[1]:
                    valid = True
        if not valid:
            result += int(k)

print(result)