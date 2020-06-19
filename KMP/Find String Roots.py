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

def solve(s):
    m = len(s)
    kmp = KMPPreprocess(s)
    while m % (m - kmp[m - 1]) != 0:
        m = kmp[m - 1]
    return len(s) // (len(s) - kmp[m - 1])

while True:
    s = input()
    if s == "*":
        break
    print(solve(s))