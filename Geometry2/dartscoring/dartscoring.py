import math

#Convex hull - The Graham scan algorithm

def leftturn(p1,p2,p3):
    cross = ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))
    if cross < 0: return True
    else: return False

# From lecture 11 Geometry
def graham(points):

    points.sort(key=lambda x:[x[0],x[1]])

    S, hull = [], []

    for p in points:
        while len(S) >= 2 and leftturn(S[-2], S[-1], p):
            S.pop()
        S.append(p)
    hull += S

    S = []
    for p in reversed(points):
        while len(S) >= 2 and leftturn(S[-2], S[-1], p):
            S.pop()
        S.append(p)

    hull += S[1:]

    return hull

def dist(p1,p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    try:
        i = [float(x) for x in input().split(" ")]
        n = int(len(i)/2)

        if n == 1:
            print(float(100))

        else:
            i = list(zip(i[::2], i[1::2]))
            res_p = graham(i)

            res = 0
            for idx in range(0,len(res_p)-1):
                res += dist(res_p[idx],res_p[idx+1])

            print((100*n)/(1+res))

    except EOFError:
         exit()

