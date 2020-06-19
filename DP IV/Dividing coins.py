def main():
    t = int(input())
    dp = [0] * 50005
    while t:
        t -= 1
        m = int(input())
        a = list(map(int, input().split()))
        sumA = sum(a)
        
        for i in range(50005):
            dp[i] = 0

        dp[0] = 1
        for i in range(m):
            for j in range(sumA, a[i] - 1, -1):
                dp[j] = dp[j - a[i]] or dp[j]
        diff = -1
        for i in range(sumA//2, -1, -1):
            if dp[i] == 1:
                diff = abs(sumA - 2 * i)
                break
        print(diff)

if __name__ == "__main__":
    main()