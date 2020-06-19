import sys
sys.setrecursionlimit(10 ** 6)

def dfs(u, graph, visited, ordering):
    global parent
    visited[u] = True

    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited, ordering)
    
    ordering.append(u)

def topological_sort(graph, ordering):
    global N
    visited = [False] * (N + 1)
    for u in range(1, N + 1):
        if not visited[u]:
            dfs(u, graph, visited, ordering)

N, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for u in range(1, K + 1):
    n, *adj_u = list(map(int, input().split()))
    graph[u] = adj_u

parent = [0] * (N + 1)
ordering = []
topological_sort(graph, ordering)

for i in range(N - 1):
    parent[ordering[i]] = ordering[i + 1]

for u in range(1, N + 1):
    print(parent[u])