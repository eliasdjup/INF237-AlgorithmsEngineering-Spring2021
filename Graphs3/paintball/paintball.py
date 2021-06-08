# Perfect matching bipartite graph
N, M = [int(x) for x in input().split()]

adj = [[] for x in range(N)]

match = {}


def checkMatch(prevMatch, newMatch):
    p = match.get(newMatch)
    if p == None:
        return True
    
    prevMatch[newMatch] = True

    for a in adj[p]:
        if (not prevMatch[a] and checkMatch(prevMatch, a)):
            match[a] = p
            return True

    return False

for i in range(M):
    A, B = [int(x) for x in input().split()]
    adj[A-1].append(B-1)
    adj[B-1].append(A-1)

for p in range(N):
    prevMatch = [False for x in range(N)] #Binary array to keep track of nodes that are matched
    for t in adj[p]:
        if (checkMatch(prevMatch, t)):
            match[t] = p
            break

if len(match) != N:
    print("Impossible")
    exit()

for i in range(N):
    print(match[i]+1)