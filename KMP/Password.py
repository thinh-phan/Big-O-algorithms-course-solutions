def KMPPreprocess(p):
    m = len(p)
    kmp = [0] * m
    i = 1
    j = 0
    while i < m:
        if p[i] == p[j]:
            j += 1
            kmp[i] = j
            i += 1
        else:
            if j == 0:
                kmp[i] = j
                i += 1
            else:
                j = kmp[j - 1]
    return kmp

s = input()
kmp = KMPPreprocess(s)
res = 0

for i in range(1, len(s) - 1):
    if kmp[i] != 0:
        if kmp[i] == kmp[-1]:
            res = kmp[i]
            break
if res == 0 and kmp[-1] != 0:
    res = kmp[kmp[-1] - 1]

print(s[:res] if res > 0 else 'Just a legend')