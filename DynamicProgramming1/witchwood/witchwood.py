# Input
N, M, K = [int(x) for x in input().split()]
TP = []
for i in range(0, M):
    T, P = [float(x) for x in input().split()]
    TP.append((T,P))


res = 0.0
for i in range(0, N):
    temp = float('inf')
    for j in range(0, M):
        local = (res+(TP[j][0])+K*(TP[j][1]))/(1-(TP[j][1]))
        temp = min(temp, local)

    res = temp
    
print(res)