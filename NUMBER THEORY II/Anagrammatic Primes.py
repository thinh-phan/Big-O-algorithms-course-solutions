def sieveOfEratosthenes(n):
    prime[0] = prime[1] = False
    i = 2
    while (i * i <= n):
        if (prime[i] == True):
            for j in range(2 * i, n + 1, i):
                prime[j] = False
        i += 1
def nextPermutation(a):
    m = len(a)
    for i in range(m - 2, -1, -1):
        if (a[i] < a[i + 1]):
            for j in range(m - 1, i, -1):
                if (a[i] < a[j]):
                    a[i], a[j] = a[j], a[i]
                    tmp = a[i+1:]
                    tmp.reverse()
                    index = 0
                    for k in range(i + 1, m):
                        a[k] = tmp[index]
                        index += 1
                    return True
    return False

def isAnaPrime(n):
    a = []
    while (n > 0):
        a.append(n % 10)
        n //= 10
    a.sort()
    m = len(a)
    for i in range(m):
        if (a[i] % 2 == 0 or (a[i] == 5 and m > 1)):
            return False
    x = True
    while(x == True or nextPermutation(a)):
        x = False
        n = 0
        for i in range(m):
            n = n * 10 + a[i]
        if (prime[n] == False): return False
    return True
def init(n):
    sieveOfEratosthenes(n)
    anaPrime.append(2)
    for i in range(3, n + 1, 2):
        if(prime[i]):
            if (isAnaPrime(i)):
                anaPrime.append(i)

maxN = 100000
prime = [True]*(maxN + 1)
anaPrime = []
init(maxN)
while(True):
    n = int(input())
    if (n == 0):
        break
    m = len(anaPrime)
    index = m - 1
    while(index >= 0 and anaPrime[index] > n):
        index -= 1
    index += 1
    if (index < m):
        pow10 = 1
        while (n > 0):
            n /= 10
            pow10 *= 10

        if (anaPrime[index] < pow10):
            print(anaPrime[index])
        else:
            print(0)
    else: 
		print(0)