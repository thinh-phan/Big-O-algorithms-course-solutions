def solve():
    n = int(input())
    if n == 0:
        exit()
    a = b = 0
    flag = 1
    for i in range(32):
        if (n >> i) & 1:
            if flag:
                a += 1 << i
            else:
                b += 1 << i
            flag ^= 1
    print(a, b)

while True:
    solve()