import bisect


def WavioLIS(a, lis):
    n = len(a)
    sub = []
    sub.append(a[0])
    for i in range(1, n):
        pos = bisect.bisect_left(sub, a[i])
        if pos == len(sub):
            sub.append(a[i])
        else:
            sub[pos] = a[i]
        lis[i] = pos + 1


def main():
    while True:
        try:
            n = int(input())
            a = list(map(int, input().split()))
            ascendingLength = [0] * n
            descendingLength = [0] * n
            WavioLIS(a, ascendingLength)
            a = list(reversed(a))
            WavioLIS(a, descendingLength)
            maxLength = 1
            for i in range(n):
                minLen = min(ascendingLength[i], descendingLength[n - i - 1])
                maxLength = max(maxLength, minLen*2 - 1)
            print(maxLength)
        except:
            exit()


if __name__ == "__main__":
    main()