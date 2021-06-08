# Time Limit Exceeded
def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

N = int(input())

data =[]

for i in range(N):
    data.append([int(x) for x in input().split()])

res = 0

N = 1 << N
for i in range(N):
    comb = []
    for j in range(N):
        if i & (1 << j) != 0:
            comb.append(data[j])
    if len(comb) == 2:
        res += dist(comb[0],comb[1])

print(res)
