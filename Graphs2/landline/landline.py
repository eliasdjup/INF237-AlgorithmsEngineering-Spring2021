# Union Find from bridges and tunnels task
parent = {}
rank = {}

def find(v):
    if v not in parent.keys():
        rank[v] = 1
        parent[v] = v
        return v
    elif parent[v] == v:
        return v
    else:
        p = find(parent[v])
        parent[v] = p
        return p

def union(a,b):
    a = find(a)
    b = find(b)

    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[b] < rank[a]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += rank[a]

#Variables
inputs = []
insecure = []
cost = 0

#Inputs ----------------------------------------
n, m, p = [int(x) for x in input().split()]

if n == 0: exit()
elif n-1 > m: print("impossible"), exit()

insecure = []
if p > 0:
    insecure = [int(x) for x in input().split()]

secures = list(range(1, n+1))
[secures.remove(x) for x in insecure]

for i in range(m):
    x, y, l = [int(x) for x in input().split()]
    inputs.append((x,y,l))
#-----------------------------------------------

#MST of secure buildings
inputs.sort(key = lambda x: x[2]) # Sort by cost
insecure_edges = []
for i in inputs:
    x, y, l = i
    a = find(x)
    b = find(y)
    if a in insecure or b in insecure:
        insecure_edges.append((x,y,l))
        continue
    if a != b:
        union(a, b)
        cost += l

# Checking that all parents of secures are the same
if len(secures) != 0:
    head = secures[0]
    for i in secures:
        if find(head) != find(i):
            print("impossible"), exit()
#--------------------------------------------------

# Connecting unsecure buildings to MST of secure buildings using the least cost edge
for (x, y, l) in insecure_edges:
    if find(x) != find(y) and (not (x in insecure and y in insecure)):
        union(x, y)
        cost += l

# All nodes are insecure
if len(insecure) == n:
    for (x, y, l) in inputs:
        if find(x) != find(y):
            union(x, y)
            cost += l

# Not all nodes are in MST
for i in range(1, n+1):
    if find(1) != find(i):
        print("impossible"), exit()

print(cost)