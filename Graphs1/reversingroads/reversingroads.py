from sys import stdin

# Iterative depth first traversal
# Reversing one of the m directed edges one by one until either all are reachable, or print 'invalid' otherwise
def DFS(node, visited, g):
    stack = [node]
    while len(stack) != 0:
        current = stack.pop()

        if current in visited:
            continue

        visited.append(current)

        # Add neighbours to stack
        for n in g[current]:
            if n not in visited:
                stack.append(n)
    return visited

def isValid(g, nodes):
        valid = True

        # Gives all edges in graph
        edges = [DFS(x, [], g) for x in range(nodes)]

        # Checking if all nodes can be reached with edges in graph
        for e in edges:
            if len(e) != nodes:
                valid = False

        return valid

def toGraph(lst):
    m,n = lst[0]
    # Initiate keys
    graph = {k:[] for k in range(m)}
    # Graphing edges between nodes
    for (a,b) in lst[1:]:
        lst = graph[a]
        lst.append(b)
        graph[a] = lst
    return graph


# Initial setup
cases = []
n_cases = 0
iterator = iter(stdin.readlines())

# Reading input
while True:
    try:
        # m : number of nodes
        # n : number of edges
        m, n = map(int, next(iterator).split())

        case_edges = []
        case_edges.append((m,n))

        for i in range(n):
            # a, b : edge from node a to b
            a,b =  map(int, next(iterator).split())
            case_edges.append((a,b))
        
        cases.append(case_edges)
        n_cases += 1

    # EOF
    except StopIteration:
        break


for c_num, c in enumerate(cases):

    c_graph = toGraph(c)
    
    # All nodes reacheable and cyclic
    if isValid(c_graph, c[0][0]): print("Case " + str(c_num + 1)+ ": valid") 

    else:
        m,n = c[0]
        # Checking if reversing one path creates a cyclic graph
        for i, (a,b) in enumerate(c[1:]):
            c[i+1] = (b,a) # Reversing (a,b)
            valid = isValid(toGraph(c), m) # Creating graph and checcking whether valid
            if valid:
                print("Case "+ str(c_num + 1)+": "+str(a)+" "+str(b))
                break
            c[i+1] = (a,b)

        # All nodes NOT reachable, even by reversing one edge
        if not valid: print("Case " + str(c_num + 1) + ": invalid")