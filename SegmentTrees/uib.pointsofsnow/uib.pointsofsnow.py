# From lecture 6 - Segment trees
def update(l, r, v, T):
    l = index(T,l)
    r = index(T,r)
    T[l] += v

    while True:
        l_parent = parent(l)
        r_parent = parent(r)
        if l_parent == r_parent:
            return
        if l % 2 == 0:
            T[right(l_parent)] += v
        if r % 2 == 1:
            T[left(r_parent)] += v
        l,r = l_parent, r_parent

def query(i, T):
    s = 0
    i = index(T, i-1)
    while i > 0:
        s += T[i]
        i = parent(i)
    print(s)


# Input
N, K, Q = [int(x) for x in input().split()]
register = [0]*(N)*2

# Also from lecture 6 - Segment trees
right = lambda i: 2 * i + 1
left = lambda i: 2 * i
parent = lambda i: i // 2
index = lambda T, i: len(T) // 2 + i


for _ in range(K + Q):
    i = input()

    if i[0] == '!':
        L, R, D = [int(x) for x in i[1:].split()]
        #Snow level rose with D cm in the area between L and the R km mark of Lineland.
        update(L,R,D, register)

    else:
        X = int(i[1:])
        #X, indicating a query requsting to know the snow depth in the middle of the X’th km of Lineland 
        query(X, register)