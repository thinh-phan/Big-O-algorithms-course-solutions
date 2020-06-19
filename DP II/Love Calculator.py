s1, s2 = None, None
m, n = None, None
scs, numWays = list(), list()

def solve():
    global s1, s2, m, n, scs, numWays
    scs.clear()
    numWays.clear()
    scs = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    numWays = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                scs[i][j] = i + j
                numWays[i][j] = 1
            elif s1[i-1] == s2[j-1]:
                scs[i][j] = scs[i-1][j-1] + 1
                numWays[i][j] = numWays[i-1][j-1]
            else:
                scs[i][j] = min(scs[i-1][j], scs[i][j-1]) + 1
                if scs[i][j] == scs[i-1][j] + 1:
                    numWays[i][j] += numWays[i-1][j]
                if scs[i][j] == scs[i][j - 1] + 1:
                    numWays[i][j] += numWays[i][j - 1]

def main():
    global s1, s2, m, n, scs, numWays
    t = int(input())
    for cs in range(1, t + 1):
        s1 = input()
        s2 = input()
        m = len(s1)
        n = len(s2)
        solve()
        print("Case {}: {} {}".format(cs, scs[m][n], numWays[m][n]))
    return 

if __name__ == "__main__":
    main()