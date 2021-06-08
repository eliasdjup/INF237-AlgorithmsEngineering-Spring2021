n = int(input())

pD = 0
pT = 0

mph = []

for _ in range(n):
    t, d = [int(x) for x in input().split()]

    deltaD = d - pD
    deltaT = t - pT

    if deltaT != 0:
        curr = deltaD // deltaT
    else:
        curr = 0
    
    mph.append(curr)

    pD = d
    pT = t

res = max(mph)

print(res)