from heapq import heappush, heappop

def topological_sort(graph, indegree, ordering):
    global N
    global names
    zero_indegree = []

    for u in range(N):
        if indegree[u] == 0:
            heappush(zero_indegree, u)
    
    while zero_indegree:
        u = heappop(zero_indegree)
        ordering.append(names[u])

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(zero_indegree, v)

tc = 1
while True:
    try:
        N = int(input())
    except EOFError:
        exit()

    vertices = dict()
    names = []
    graph = [[] for _ in range(N)]
    indegree = [0] * N

    for i in range(N):
        beverage = input()
        vertices[beverage] = i
        names.append(beverage)

    M = int(input())
    for _ in range(M):
        beverage_1, beverage_2 = input().split()
        u, v = vertices[beverage_1], vertices[beverage_2]
        graph[u].append(v)
        indegree[v] += 1

    ordering = []
    topological_sort(graph, indegree, ordering)

    print('Case #{}: Dilbert should drink beverages in this order: '.format(tc), end='')
    print(*ordering, end='.\n\n')
    tc += 1
    input()