instuff = open("passport.in", "r")
instuff1 = instuff.readlines()

passports = []
passport = ""

for i in instuff1:
    if len(i) == 1:
        passports.append(passport)
        passport = ""
    else:
        passport += i

for i in range(len(passports)):
    np = ""
    for k in passports[i].split("\n"):
        np += k + " "
    passports[i] = np[:-1]

res = 0
for p in passports:
    result = True
    for i in p.split(" ")[:-1]:
        key = i.split(":")[0]
        val = i.split(":")[1]
        if key == "byr" and not (
            len(val) == 4 and int(val) >= 1920 and int(val) <= 2002
        ):
            result = False
        elif key == "iyr" and not (
            len(val) == 4 and int(val) >= 2010 and int(val) <= 2020
        ):
            result = False

        elif key == "eyr" and not (
            len(val) == 4 and int(val) >= 2020 and int(val) <= 2030
        ):
            result = False
        elif key == "hgt" and not (
            (
                (val[-2:] == "in" and int(val[:-2]) >= 59 and int(val[:-2]) <= 76)
                or (val[-2:] == "cm" and int(val[:-2]) >= 150 and int(val[:-2]) <= 193)
            )
        ):
            result = False
        elif key == "ecl" and not (
            (
                "amb" == val
                or "blu" == val
                or "brn" == val
                or "gry" == val
                or "grn" == val
                or "hzl" == val
                or "oth" == val
            )
        ):

            result = False
        if key == "hcl":
            if val[0] == "#":
                for j in val[1:]:
                    if not (
                        j == "a"
                        or j == "b"
                        or j == "c"
                        or j == "d"
                        or j == "e"
                        or j == "f"
                    ):
                        try:
                            int(j)
                        except ValueError:
                            result = False
                            break
            else:
                result = False
        if key == "pid":
            if len(val) == 9:
                try:
                    int(val)
                except ValueError:
                    result = False
            else:
                result = False
    for i in ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]:
        if i not in p:
            result = False
    if result:
        res += 1
print(res)
