isPrime = [True for _ in range(1001)]

isPrime[0] = False
isPrime[1] = True

for i in range(2, 1001):
    if isPrime[i]:
        for j in range(i * i, 1001, i):
            isPrime[j] = False

while True:
    try:
        n, c = map(int, input().strip().split())

        primes = []
        for i in range(1, n + 1):
            if isPrime[i]:
                primes.append(i)

        m = len(primes)
        print('{0} {1}:'.format(n, c), end='')

        if m < (2 * c - 1):
            for prime in primes:
                print(' {0}'.format(prime), end='')
        else:
            for i in range(m // 2 - c + (m % 2), m // 2 + c):
                print(' {0}'.format(primes[i]), end='')
        print('\n')
    except Exception as e:
        break