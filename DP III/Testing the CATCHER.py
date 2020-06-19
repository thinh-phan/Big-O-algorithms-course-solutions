def main():
    test = 0
    while True:
        a = []
        x = int(input())
        if x == -1:
            break

        if test != 0:
            print()

        a.append(x)
        while True:
            x = int(input())
            if x == -1:
                break
            a.append(x)

        # Longest decreasing sub
        f = [1 for _ in range(len(a) + 1)]
        ans = 1
        for i in range(1, len(a)):
            for j in range(i):
                if a[j] >= a[i]:
                    f[i] = max(f[i], f[j] + 1)
            ans = max(ans, f[i])

        test += 1
        print("Test #{}:".format(test))
        print("  maximum possible interceptions: {}".format(ans))
        a.clear()


if __name__ == "__main__":
    main()