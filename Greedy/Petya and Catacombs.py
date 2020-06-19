n = int(input())
tmp = list(map(int, input().split()))

t = [0] * (n + 1)
for x in tmp:
    t[x] = 1

count = 1
for i in range(n):
    if not t[i]:
        count += 1

print(count)