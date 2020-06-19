MAX = 6100
max_palin_length = [[0] * MAX for i in range(MAX)]

def main():
    t = 1

    for test_case in range(t):
        s = input()
        n = len(s)


        for i in range(n):
            max_palin_length[i][i] = 1

        if n > 1:
            for i in range(n - 1):
                if s[i] == s[i + 1]:
                    max_palin_length[i][i + 1] = 2
                else:
                    max_palin_length[i][i + 1] = 1

        for length in range(3, n + 1):
            for start in range(0, n - length + 1):
                end = start + length - 1

                if s[start] == s[end]:
                    max_palin_length[start][end] = max_palin_length[start + 1][end - 1] + 2
                else:
                    max_palin_length[start][end] = max(max_palin_length[start + 1][end],
                                                       max_palin_length[start][end - 1])

        ans = n - max_palin_length[0][n - 1]
        print(ans)


if __name__ == "__main__":
    main()