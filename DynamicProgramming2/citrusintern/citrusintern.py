#  Minimum weight vertex cover
N = int(input())
cost = []
adj = [[] for _ in range(N)]
root = [True]*N

for i in range(N):
    ln = [int(x) for x in input().split()]
    cost.append(ln[0])

    if ln[1] == 0:
        continue

    for j in range(2,ln[1]+2):
        adj[i].append(ln[j])
        root[ln[j]] = False


for i in range(N):
    if root[i]:
        r = i
        break

down = [0]*N
up = [0]*N


def fill(current):
    if adj[current] == []:
        down[current] = float('inf')
        return
    
    delta = float('inf')

    for n in adj[current]:
        fill(n)

        cost[current] += up[n]

        up[current] += min(cost[n], down[n])
        down[current] += min(cost[n], down[n])

        delta = min(max(cost[n]- down[n],0),delta)
    
    down[current] += delta

fill(r)

print(min(down[r],cost[r]))