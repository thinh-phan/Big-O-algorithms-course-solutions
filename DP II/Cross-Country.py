def main():
    global reader
    reader = Reader()

    d = int(reader.next())

    for i in range(d):
        solve_data_set()


def solve_data_set():
    agnes_route = []
    agnes_route.append(0)

    while True:
        point = int(reader.next())

        if point == 0:
            break

        agnes_route.append(point)

    tom_routes = []

    while True:
        route = []
        route.append(0)

        while True:
            point = int(reader.next())

            if point == 0:
                break

            route.append(point)

        if len(route) == 1:
            break

        tom_routes.append(route)

    ans = 0

    for route in tom_routes:
        ans = max(ans, lcs(route, agnes_route))

    print(ans)


def lcs(route, agnes_route):
    n = len(route) - 1
    m = len(agnes_route) - 1
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if route[i] == agnes_route[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


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