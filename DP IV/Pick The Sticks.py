MAX_N = 1005
MAX_L = 4005

class item:
    def __init__ (self, l, v):
        self.l = l
        self.v = v

test = int(input())
for tt in range(test):
    x = input()
    a = []
    a.append(item(0, 0))
    res = -1
    n, L = map(int, input().split())
    L = L * 2
    for i in range(1, n + 1):
        l, v = map(int, input().split())
        a.append(item(l, v))
        res = max(res, a[i].v)

    f = [[[0 for c in range(3)] for j in range(L + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, L + 1):
            for c in range(3):
                f[i][j][c] = f[i - 1][j][c]
                if j >= 2 * a[i].l:
                    f[i][j][c] = max(f[i][j][c], f[i - 1][j - 2 * a[i].l][c] + a[i].v)
                if j >= a[i].l and c > 0:
                    f[i][j][c] = max(f[i][j][c], f[i - 1][j - a[i].l][c - 1] + a[i].v)
    
    for c in range(3):
        res = max(res, f[n][L][c])
    
    print("Case #", end = "")
    print(tt + 1, end = ": ")
    print(res)