def main():
    reader = Reader()

    N = 100
    global text1
    text1 = [None for i in range(N + 1)]
    global text2
    text2 = [None for i in range(N + 1)]

    while True:
        word = reader.next()
        if word == None:
            break

        n = 0
        m = 0

        while word != '#':
            n += 1
            text1[n] = word
            word = reader.next()

        word = reader.next()
        while word != '#':
            m += 1
            text2[m] = word
            word = reader.next()

        global dp
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        global answer
        answer = []
        trace(n, m)

        print(answer[0], end='')
        for i in range(1, len(answer)):
            print(" {0}".format(answer[i]), end='')
        print()


def trace(i, j):
    if i == 0 or j == 0:
        return

    if text1[i] == text2[j] and dp[i][j] == dp[i - 1][j - 1] + 1:
        trace(i - 1, j - 1)
        answer.append(text1[i])
    elif dp[i][j] == dp[i - 1][j]:
        trace(i - 1, j)
    else:
        trace(i, j - 1)


class Reader:
    def __init__(self):
        self.tokens = []
        self.index =  0

    def next(self):
        self.index += 1

        if self.index >= len(self.tokens):
            try:
                self.tokens = input().split()
            except EOFError:
                return None
            self.index = 0

        return self.tokens[self.index]


if __name__ == "__main__":
    main()