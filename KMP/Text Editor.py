def KMPPreprocess(s):
    m = len(s)
    prefix = [0] * m
    i = 1
    j = 0
    while i < m:
        if s[i] == s[j]:
            j += 1
            prefix[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                prefix[i] = 0
                i += 1
    return prefix

def KMPSearch(t, p, prefix, m):
    n = len(t)
    cnt = 0
    i = j = 0
    while i < n:
        if p[j] == t[i]:
            j += 1
            i += 1
        if j == m:
            cnt += 1
            j = prefix[j - 1]
        else:
            if i < n and p[j] != t[i]:
                if j != 0:
                    j = prefix[j - 1]
                else:
                    i += 1
    return cnt

t = input()
p = input()
k = int(input())
l, r = 0, len(p) - 1

ans = 0
prefix = KMPPreprocess(p)
while l <= r:
    mid = (l + r) // 2
    cnt = KMPSearch(t, p, prefix, mid + 1)
    if cnt >= k:
        ans = mid + 1
        l = mid + 1
    else:
        r = mid - 1

print(p[:ans] if ans > 0 else 'IMPOSSIBLE')