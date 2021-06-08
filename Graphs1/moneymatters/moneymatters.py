'''
Money Matters,  see if the sum of vertex weights of each CC = 0
n : number of friends
m : number of remaining friendships
o : credit or debit of each person
x, y : indicating that persons x and y are still friends.
'''

# Initial setup
n, m = map(int, input().split())

o = [] # List of debt
for i in range(n):
    o.append(int(input()))

g = {} # graph of relations
for i in range(m):
    x,y = map(int, input().split())

    #x
    f = g.get(x, [])
    f.append(y)
    g[x] = f

    #y
    f = g.get(y, [])
    f.append(x)
    g[y] = f



def traverse(g,o,n):
    v = set() # visited nodes in graph

    # f : friend
    for f in range(n): 
        if f in v:
            continue

        # If friend not present in the graph of relations and the friend has credit/debit the equation is impossible
        if f not in g.keys():
            if o[f] != 0:
                return False
            continue

        #Iterativly traverse g with stack
        stack = [f]
        sum = 0
        while len(stack) != 0:
            c = stack.pop() # Current node in traversal
            if c in v: 
                continue
            v.add(c)
            sum += o[c]
            # Add neighbours to stack
            for n in g[c]:
                if n not in v:
                    stack.append(n)

        # If sum of credit and debit not equal to 0 the equation is impossible
        if sum != 0:
            return False

    return True

# Main
print ("POSSIBLE") if traverse(g,o,n) else print ("IMPOSSIBLE")
