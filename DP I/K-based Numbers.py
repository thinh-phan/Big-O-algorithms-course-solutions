N = int(input())
K = int(input())

if N == 1:
    print(K)
else:
    endWith0 = [0]*20
    endNot0 = [0]*20
    endNot0[1] = K-1
    for i in range(2, N+1):
        endWith0[i] = endNot0[i-1]
        endNot0[i] = (endNot0[i-1] + endWith0[i-1]) * (K-1)
    print(endNot0[N]+ endWith0[N])