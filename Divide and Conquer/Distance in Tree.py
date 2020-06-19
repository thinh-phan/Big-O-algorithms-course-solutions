import sys
sys.setrecursionlimit(1000000)
def get(graph, u, par):
    count = {0: 1}
    res = 0
    for v in graph[u]:
        if v != par:
            res_v, count_v = get(graph, v, u)
            res += res_v

            count_v[-1] = 0

            for key, val in count_v.items():
                res += val * count.get(k - 1 - key, 0)

            for key, val in count_v.items():
                count[key + 1] = count.get(key + 1, 0) + val
    
    return res, count

n, k = map(int, input().split())

graph = [[] for i in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

print(get(graph, 0, -1)[0])