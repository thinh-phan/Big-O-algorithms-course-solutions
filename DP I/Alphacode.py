MAX_N = 5005

if __name__ == '__main__':
    while 1:
        s = input()
        if s == '0':
            break

        n = len(s)
        f = [0] * MAX_N
        f[0] = 1
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] = f[i - 1]

            if i > 1 and s[i - 2] != '0':
                val = (ord(s[i - 2]) - ord('0')) * 10 + ord(s[i - 1]) - ord('0')
                if val <= 26:
                    f[i] += f[i - 2]

        print(f[n])