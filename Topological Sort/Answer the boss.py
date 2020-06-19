def main():
    t = int(input())
    for testNumber in range(1, t + 1):
        solveTest(testNumber)


def solveTest(testNumber):
    n, r = map(int, input().split())

    adj = [[] for u in range(n)]
    in_deg = [0 for u in range(n)]

    for i in range(r):
        u, v = map(int, input().split())
        adj[v].append(u)
        in_deg[u] += 1
    
    topo_order = topo_sort(adj)
    rank = [0 for i in range(n)]

    for u in topo_order:
        if in_deg[u] == 0:
            rank[u] = 1
        for v in adj[u]:
            rank[v] = max(rank[v], rank[u] + 1)
    
    employees = [Employee(u, rank[u]) for u in range(n)]
    employees.sort(key=lambda e: (e.rank, e.index))

    print("Scenario #{0}:".format(testNumber))

    for e in employees:
        print("{0} {1}".format(e.rank, e.index))
    

def topo_sort(adj):
    topo_order = []
    n = len(adj)
    visited = [False for u in range(n)]

    for u in range(n):
        if not visited[u]:
            dfs(u, adj, visited, topo_order)
    
    topo_order.reverse()

    return topo_order


def dfs(u, adj, visited, topo_order):
    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            dfs(v, adj, visited, topo_order)
    
    topo_order.append(u)


class Employee:
    def __init__(self, index, rank):
        self.index = index
        self.rank = rank


if __name__ == "__main__":
    main()