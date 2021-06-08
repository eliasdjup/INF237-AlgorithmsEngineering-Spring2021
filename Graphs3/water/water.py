from collections import deque

class Graph():
    def __init__(self, graph):
        self.residual = graph
        self.V = [i for i in range(len(graph))]

    def edge(self, a, b, c):
        self.residual[a-1][b-1] += c
        self.residual[b-1][a-1] += c

    # From lecture 10 - Flow
    def bfs(self, start, target):
        q = deque([start])
        parents = dict()
        while q:
            v = q.popleft()
            for u in self.V:
                if u in parents:
                    continue
                if self.residual[v][u] <= 0:
                    continue
                parents[u] = v
                q.append(u)
                if u == target:
                    # Path creation
                    path = [target]
                    while target != start:
                        target = parents[target]
                        path.append(target)
                    return tuple(reversed(path))

    # From lecture 10 - Flow
    def maxflow(self, start, target):
        flow = 0
        P = self.bfs(start,target)
        while P != None:
            F = min(self.residual[v][u] for (v, u) in tail(P))
            flow += F
            for i in range(1, len(P)):
                v, u = P[i - 1], P[i]
                self.residual[v][u] -= F
                self.residual[u][v] += F
            P = self.bfs(start,target)
        return flow


n, p, k = [int(x) for x in input().split()]
g = Graph([[0]*n for x in range(n)])

tail = lambda p: zip(p, p[1:])

for i in range(p):
    a, b, c = [int(x) for x in input().split()]
    g.edge(a,b,c)

current = g.maxflow(0,1)
print(current)

for i in range(k):
    a, b, c = [int(x) for x in input().split()]

    capacity = g.residual[a-1][b-1] == 0 or g.residual[b-1][a-1] == 0
    g.edge(a,b,c)

    if capacity:
        current += g.maxflow(0,1)
    print(current)