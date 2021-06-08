# Chromatic number
# The chromatic number of a graph is the smallest number of colors needed to color the vertices of so that no two adjacent vertices share the same color

def possibleColors(c, num_colors):
    l = [x for x in range(n) if c[x] == -1]

    if len(l) == 0:
        return True
    else:
         current = l[0]

    s = set(c[i] for i in adj[current] if c[i] != -1)
    possible = [x for x in range(num_colors) if x not in s]

    for id in possible:
        c[current] = id

        if possibleColors(c, num_colors):
            return True

        c[current] = -1
    return False

n = int(input())
adj = [[]] * n

for v in range(n):
    adj[v] = [int(x) for x in input().split()]

num_colors = 1

color = [-1] * n
color[0] = 0
color[adj[0][0]] = 1

cont = True
while cont:
    num_colors += 1
    cont = not possibleColors(color.copy(), num_colors)

print(num_colors)