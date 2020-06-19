def solve():
    h, w = map(int, input().split())
    
    floor = []
    for i in range (0, h):
        floor.append(list(map(int, input().split())))

    dp = [row[:] for row in floor]
    for i in range(1, h):
        for j in range(0, w):
            a = b = c = -1
            if (j > 0):
                a = dp[i-1][j-1]
            if (j < w-1):
                b = dp[i-1][j+1]
            c = dp[i-1][j]
            dp[i][j] += max(a, b, c)
    
    print(max(dp[h-1]))

##----------------------------------------------------

t = int(input())
while (t > 0):
    t -= 1
    solve()