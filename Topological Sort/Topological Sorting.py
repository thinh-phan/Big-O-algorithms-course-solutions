import queue


def topoSort(adj, indegree):
    zero_indegree = queue.PriorityQueue()
    topoSorted = []

    for i in range(n):
        if indegree[i] == 0:
            zero_indegree.put(i)

    while not zero_indegree.empty():
        u = zero_indegree.get()
        topoSorted.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.put(v)

    return topoSorted


def main():
    global n, m
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]

    for i in range(m):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        indegree[v-1] += 1

    res = topoSort(adj, indegree)
    if (len(res) < n):
        print("Sandro fails.")
        return 0

    for i in range(n):
        print("{} ".format(res[i] + 1), end="")


if __name__ == "__main__":
    main()