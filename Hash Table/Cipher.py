def solve():
    n, k = map(int, input().split())
    s = list(map(int, list(input())))
    res = []
    sum_xor = 0
    c = 0
    for i in range(n):
        if i >= k:
            c ^= res[i - k]
        cur = c ^ s[i]
        c ^= cur
        res.append(cur)
    print(''.join(map(str, res)))

solve()