class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def get_time(turn_time):
    start_time, end_time = input().split()
    hour, minute = map(int, start_time.split(':'))
    start_minute = hour*60 + minute
    hour, minute = map(int, end_time.split(':'))
    end_minute = hour*60 + minute + turn_time
    return start_minute, end_minute

# main function


def main():
    T = int(input())
    for p in range(T):
        trip = [[] for i in range(2)]

        turn_time = int(input())
        n = list(map(int, input().split()))
        print("Case #{}:".format(p+1), end='')
        for j in range(2):
            for _ in range(n[j]):
                start, end = get_time(turn_time)
                trip[j].append(Pair(start, end))

        result = n[:]
        for j in range(2):
            waiting = j
            travelling = (j+1) % 2
            trip[waiting].sort(key=lambda x: x.first)
            trip[travelling].sort(key=lambda x: x.second)
            i1 = i2 = 0
            while i1 < n[waiting] and i2 < n[travelling]:
                if trip[waiting][i1].first >= trip[travelling][i2].second:
                    result[waiting] -= 1
                    i2 += 1
                i1 += 1
        print(" {} {}".format(result[0], result[1]))


main()