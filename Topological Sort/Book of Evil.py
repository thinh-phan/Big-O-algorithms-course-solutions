import sys
sys.setrecursionlimit(10000000)

def computeMaxUp(src, par):
    max1 = -1
    max2 = -1
    for v in graph[src]:
        if v == par:
            continue
        if maxDown[v] > max1:
            max2 = max1
            max1 = maxDown[v]
        elif maxDown[v] > max2:
            max2 = maxDown[v]

    for v in graph[src]:
        if v == par:
            continue
        maxUp[v] = max2 if maxDown[v] == max1 else max1
        if maxUp[v] != -1: # in case of root node or sibling node have no affective node
            maxUp[v] += 2
        if maxUp[src] != -1: # in case of root node...
            maxUp[v] = max(maxUp[v], maxUp[src] + 1);
        if affected[v]:
            maxUp[v] = max(maxUp[v], 0);
        computeMaxUp(v, src);

def computeMaxDown(src, par):
    maxDown[src] = 0 if affected[src] else -1

    for v in graph[src]:
        if v == par:
            continue
        d = computeMaxDown(v, src)
        if d > -1:
            maxDown[src] = max(maxDown[src], d + 1)
    return maxDown[src]
    
if __name__ == "__main__":
    n, m, d = map(int, input().split())

    affected = [False] * n
    for p in map(int, input().split()):
        affected[p - 1] = True

    graph = [[] for i in range(n)]
    for i in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    maxDown = [0] * n
    computeMaxDown(0, -1)

    maxUp = [0] * n
    maxUp[0] = 0 if affected[0] else -1
    computeMaxUp(0, -1)

    ans = len([i for i in range(n) if maxDown[i] <= d >= maxUp[i]])
    print(ans)