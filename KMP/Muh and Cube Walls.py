def KMPPreprocess(p, prefix):
    m = len(p)
    prefix = [0] * m
    j = 0
    i = 1
    while i < m:
        if p[i] == p[j]:
            j += 1
            prefix[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                prefix[i] = 0
                i += 1
    return prefix

def calc(B, A):
    if len(B) == 0:
        return len(A) + 1

    prefix = []
    prefix = KMPPreprocess(B, prefix)

    cnt = 0

    n = len(A)
    m = len(B)
    i, j = 0, 0
    while i < n:
        if B[j] == A[i]:
            i += 1
            j += 1
        if j == m:
            cnt += 1
            j = prefix[j - 1]
        elif i < n and B[j] != A[i]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return cnt

if __name__ == '__main__':
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    A = []
    for i in range(n - 1):
        x = a[i + 1] - a[i]
        A.append(x)

    B = []
    for i in range(w - 1):
        x = b[i + 1] - b[i]
        B.append(x)

    print(calc(B, A))