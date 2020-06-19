import sys
sys.setrecursionlimit(10**6)

MAX_OXI = 22
MAX_NITRO = 80
INF = 1000000000


def solve(i, oxiNeed, nitroNeed):
    global dp, oxiCylinder, nitroCylinder, weight

    if dp[i][oxiNeed][nitroNeed] != -1:
        return dp[i][oxiNeed][nitroNeed]

    if oxiNeed == 0 and nitroNeed == 0:
        dp[i][oxiNeed][nitroNeed] = 0
        return dp[i][oxiNeed][nitroNeed]

    if i == 0:
        dp[i][oxiNeed][nitroNeed] = INF
    else:
        donTakeThisCylinder = solve(i-1, oxiNeed, nitroNeed)

        newOxiNeed = max(oxiNeed - oxiCylinder[i], 0)
        newNitroNeed = max(nitroNeed - nitroCylinder[i], 0)
        takeThisCylinder = solve(i-1, newOxiNeed, newNitroNeed) + weight[i]

        dp[i][oxiNeed][nitroNeed] = min(donTakeThisCylinder, takeThisCylinder)

    return dp[i][oxiNeed][nitroNeed]


def main():
    global dp, oxiCylinder, nitroCylinder, weight

    T = int(input())
    while T > 0:
        oxi, nitro = map(int, input().split())
        n = int(input())

        oxiCylinder = [0 for i in range(n+1)]
        nitroCylinder = [0 for i in range(n+1)]
        weight = [0 for i in range(n+1)]
        dp = [[[-1 for k in range(MAX_NITRO)] for j in range(MAX_OXI)] for i in range(n+1)]

        for i in range(1, n+1):
            oxiCylinder[i], nitroCylinder[i], weight[i] = map(int, input().split())

        solve(n, oxi, nitro)
        print(dp[n][oxi][nitro])

        T -= 1
        try:
            x = input()
        except EOFError:
            pass


if __name__ == "__main__":
    main()