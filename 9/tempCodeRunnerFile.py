for i in range(len(instuff1) - 1):
    for j in range(i + 1, len(instuff1) - 1):
        sumi = 0
        for k in range(i, j):
            sumi += instuff1[k]
        if sumi == result:
            mini = instuff1[i]
            maxi = instuff1[i]
            for k in range(i, j):
                mini = min(mini, instuff1[k])
                maxi = max(maxi, instuff1[k])
            print(mini + maxi)
        elif sumi > result:
            break