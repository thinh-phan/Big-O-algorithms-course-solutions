def solve():
    try:
        a, b = input().split()
    except Exception:
        exit()
    
    n = len(a)
    m = len(b)
    a = '#' + a
    b = '#' + b

    lcs = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i] == b[j]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    res = ""
    i = n
    j = m
    while i > 0 or j > 0:
        if i == 0:
            res += b[j]
            j -= 1
        elif j == 0:
            res += a[i]
            i -= 1
        else:
            if a[i] == b[j]:
                res += a[i]
                i -=1
                j -= 1
            elif lcs[i][j] == lcs[i - 1][j]:
                res += a[i]
                i -= 1
            else:
                res += b[j]
                j -= 1
    
    print(res[::-1])

while True:
    solve()