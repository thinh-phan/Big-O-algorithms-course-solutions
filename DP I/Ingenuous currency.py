import sys

dp = [0]*10000
dp[0] = 1
for j in range(1, 22):
    W = j**3
    for i in range(W, 10000):
        dp[i] += dp[i-W]
        
inp = map(int, sys.stdin.read().split())
for n in inp:
    print(dp[n])