n, m = map(int, input().split())
T = [0] * (1 << (n + 1))

arr = list(map(int, input().split()))
for i in range(1 << n, 1 << (n + 1)):
        T[i] = arr[i - (1 << n)];
        p = i // 2
        t = 1
        while p > 0:
                T[p] = T[p << 1] | T[p << 1 | 1] if t == 1 else T[p << 1] ^ T[p << 1 | 1]
                p //= 2
                t ^= 1
        
while m > 0:
        p, b = map(int, input().split())
        p = (p + (1 << n) - 1)
        T[p] = b
        p //= 2
        t = 1
        while p > 0:
                T[p] = T[p << 1] | T[p << 1 | 1] if t == 1 else T[p << 1] ^ T[p << 1 | 1]
                p //= 2
                t ^= 1
        
        print(T[1])
        m -= 1