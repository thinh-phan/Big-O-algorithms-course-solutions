while True:
    n = int(input())
    if n == 0:
        break
    
    res = s = 0

    for x in list(map(int, input().split())):
        res += abs(s)
        s += x
    print(res)