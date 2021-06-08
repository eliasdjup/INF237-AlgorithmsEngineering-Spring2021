parent = {}
rank = {}

# Mapping buildings to integer IDs; Union Find; size of set

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

    if a == b:
        print(rank[a])
        return

    if rank[a] <= rank[b]:
        parent[a] = b
        rank[b] += rank[a]
        print(rank[b])
        return
    
    elif rank[b] < rank[a]:
        parent[b] = a
        rank[a] += rank[b]
        print(rank[a])
        return

n = int(input())

for i in range(n):
    a,b = input().split(" ")
    union(a,b)