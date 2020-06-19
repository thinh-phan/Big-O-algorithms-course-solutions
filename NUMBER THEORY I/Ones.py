if __name__ == '__main__':
    while(True):
        try:
            n = int(input())
        except EOFError:
            import sys
            sys.exit()
        b = 1
        cnt = 1
        while b % n != 0:
            b = b *10 + 1
            b %= n
            cnt += 1
        print(cnt)