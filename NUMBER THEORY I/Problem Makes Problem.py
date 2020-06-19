maxx = 20000001
mod = 1000000007
fact = [0] * maxx

def init():
    fact[0] = 1
    for i in range(1, maxx):
        fact[i] = (i * fact[i - 1]) % mod

def modularExponentiation(a, b):
    res = 1
    a %= mod
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % mod
        b //= 2
        a = (a * a) % mod
    return res

def modInverse(b):
    return modularExponentiation(b, mod - 2)

def getC(n, k):
    nu = fact[n+k-1]
    de = fact[n] * fact[k-1] % mod
    return nu * modInverse(de) % mod

if __name__ == '__main__':
    init()
    test = int(input())
    for tt in range(1, test+1):
        n, k = map(int, input().split())
        print("Case {}: {}".format(tt, getC(n, k)))