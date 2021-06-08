# Time Limit Exceeded
def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

N = int(input())

lst =[[int(x) for x in input().split()]]

res = 0

for i in range(N-1):
    inp = ([int(x) for x in input().split()])
    for pos in lst:
        res += dist(inp,pos)
    lst.append(inp)

print(res)