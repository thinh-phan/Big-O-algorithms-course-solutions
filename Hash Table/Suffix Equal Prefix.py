MOD = 10 ** 9 + 7
MAXN = 10 ** 6 + 1
f = MAXN * [0]
mul = MAXN * [0]

def polyHash(keys):
    hashValue = 0
    n = len(keys)
    for i in range(n):
        hashValue = (ord(keys[i]) - 97 + (26 * hashValue) % MOD) % MOD
        f[i + 1] = hashValue

mul[0] = 1
for i in range(1, MAXN):
    mul[i] = (mul[i - 1] * 26) % MOD

test = int(input())
for t in range(1, test + 1):
    s = input()
    f[0] = 0
    n = len(s)
    polyHash(s)
    res = 0
    length = 1
    while length < n:
        if f[length] == ((f[n] - (f[n - length] * mul[length]) % MOD) + MOD) % MOD:
            res += 1
        length += 1
    print("Case", t, end = "")
    print(":", res)