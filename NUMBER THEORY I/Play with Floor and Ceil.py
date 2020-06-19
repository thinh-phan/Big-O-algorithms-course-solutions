def extendedEuclid(a, b):
    global X, Y
    if a == 0:
        X, Y = 0, 1
        return [b, X, Y]

    temp = extendedEuclid(b % a, a)
    X = temp[2] - (b // a) * temp[1]
    Y = temp[1]
    return [temp[0], X, Y]

if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        x, k = map(int, input().split())
        p, q = 0, 0
        r = x % k
        if r == 0:
            p, q = k, 0
        else:
            a = x // k
            b = a + 1
            temp = extendedEuclid(abs(a), abs(b))
            g = temp[0]
            x0 = temp[1]
            y0 = temp[2]
            x0 *= x // g
            y0 *= x // g
            if a < 0:
                x0 = -x0

            if b < 0:
                y0 = -y0

            p, q = x0, y0
        print(p, q)
        
#solution bo sung
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        x, k = map(int, input().split())
        r = x % k
        if r == 0:
            p = k
            q = 0
        else:
            a = x // k
            p = 1 + a - x
            q = x - a
        print(p, q)