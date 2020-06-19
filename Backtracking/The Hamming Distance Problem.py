def check(n, h, idx, start, res):
    if idx == h:
        print(''.join(res))
        return
    for i in range(n - h + idx, start - 1, -1):
        res[i] = '1'
        check(n, h, idx + 1, i + 1, res)
        res[i] = '0'
def solve():
    input()
    n, h = map(int, input().split())
    res = ['0'] * n
    check(n, h, 0, 0, res)

t = int(input())
for tc in range(t):
    solve()
    if tc < t - 1:
        print()