from collections import namedtuple as T
from collections import defaultdict as D
import itertools as IT
import math
import sys

# Travelling salesman problem

Set = frozenset
Place = T("Place", "name x y")
INF = float('inf')
Sol = T("Sol", "cost path")

def dist(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

def powerset(S):
    for k in range(len(S)):
        for SS in IT.combinations(S, k):
            yield Set(SS)

def tsp(errands, start, end):
    DP = D(lambda : (INF, None))
    for v in errands:
        DP[Set([v]), v] = Sol(dist(start, v), [start,v])

    V = Set(errands)

    for set_s in powerset(V):
        for v in set_s:
            v_sol = DP[set_s, v]
            for u in errands:
                if u in set_s:
                    continue
                set_su = set_s | Set([u])

                c_sol = DP[set_su, u]
                n_cost = v_sol.cost + dist(v,u)


                if n_cost < c_sol[0]:
                    DP[set_su, u] = Sol(n_cost, v_sol.path + [u])

    opt = Sol(INF, None)

    for v in errands:
        cur = DP[Set(errands), v]

        if cur.cost + dist(v, end) < opt.cost:
            opt = Sol(cur.cost + dist(v, end), cur.path + [end])
        

    return opt


n = int(input())
home = None
work = None
locations = dict()
for i in range(n):
    name, x, y= input().split()
    if name == "home":
        home = Place(name, float(x), float(y))
        continue
    if name == "work":
        work = Place(name, float(x), float(y))
        continue
    else:
        locations[name] = Place(name, float(x), float(y))


try:
    while True:
        inp = input().split()

        errands = []
        for e in inp:
            errands.append(locations[e])
        
        res = tsp(errands, work, home)

        p = []
        for r in res.path:
            p.append(r.name)
        
        print(*p[1:-1])

except EOFError:
    exit()