MAX = 10**7 + 1
dp = [-1]*MAX

def solve(n):
    if (n < MAX and dp[n] != -1):
        return dp[n]
    if (n < 3):
        return n
    result = max(solve(n//2) + solve(n//3) + solve(n//4), n);
    if n < MAX:
        dp[n] = result
    return result

if __name__ == '__main__':
    while(True):
        try:
            n = int(input())
        except EOFError:
            import sys
            sys.exit()
        print(solve(n))