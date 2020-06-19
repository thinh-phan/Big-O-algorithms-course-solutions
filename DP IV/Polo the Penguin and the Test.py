import sys
sys.setrecursionlimit(100000)

# main function
def main():
    N = 109
    
    T = int(input())

    for test_case in range(T):
        n, w = map(int, input().strip().split())
        c = []
        p = []
        t = []
        c.append(0)
        p.append(0)
        t.append(0)
        for i in range(n):
            x, y, z = map(int, input().strip().split())
            c.append(x)
            p.append(y)
            t.append(z)

        dp = [[0 for i in range(N)] for j in range(N)]
        for i in range(1, n + 1):
            for j in range(w + 1):
                if t[i] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - t[i]] + c[i] * p[i])
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp[n][w])

if __name__ == "__main__":
    main()