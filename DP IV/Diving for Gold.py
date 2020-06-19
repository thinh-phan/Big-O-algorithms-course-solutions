import sys

class Treasure:
    def __init__(self, time, gold, id):
        self.time = time
        self.gold = gold
        self.id = id


def main():
    newline = False

    while True:
        t, w = map(int, input().split())
        n = int(input())

        treasure = []
        for i in range(n):
            time, gold = map(int, input().split())
            treasure.append(Treasure(time, gold, i))

        collect = [[0 for j in range(t+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, t+1):
                if j < treasure[i - 1].time * w * 3:
                    collect[i][j] = collect[i - 1][j]
                else:
                    collect[i][j] = max(collect[i - 1][j], collect[i - 1][j - treasure[i - 1].time * w * 3] + treasure[i - 1].gold)

        if newline:
            print()
        newline = True

        print(collect[n][t])
        pick_list = []
        for i in range(n, 0, -1):
            if collect[i][t] != collect[i - 1][t]:
                pick_list.append(treasure[i - 1].id)
                t -= treasure[i - 1].time * w  * 3

        print(len(pick_list))
        for i in range(len(pick_list) - 1, -1, -1):
            print(treasure[pick_list[i]].time, treasure[pick_list[i]].gold)

        try:
            input()
        except EOFError:
            break

if __name__ == "__main__":
    main()