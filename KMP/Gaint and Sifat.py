def KMPPreprocess(p):
    m = len(p)
    prefix = [0] * m
    i = 1
    j = 0
    while i < m:
        if p[i] == p[j]:
            j += 1
            prefix[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix[j-1]
            else:
                prefix[i] = 0
                i+=1
    return prefix

def KMPSearch(t, p, prefix):
    n, m = len(t), len(p)
    i = j = 0
    res = 0
    while i < n:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = prefix[j - 1]
        if j == m:
            res += 1
            j = prefix[j - 1]
    return res
def solve(S, s):
    S = S.replace(' ', '')
    s = s.replace(' ', '')
    prefix = KMPPreprocess(s)
    return KMPSearch(S, s, prefix)

T = int(input())
for t in range(T):
    S = input().strip()
    s = input().strip()
    print('Case {}: {}'.format(t + 1, solve(S, s)))