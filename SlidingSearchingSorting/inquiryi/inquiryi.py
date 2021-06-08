# Sliding window; maintain left and right pointers

from sys import stdin

iterator = iter(stdin.readlines())
seq=[]
n = int(next(iterator))

for idx in range(0,n):
    a = int(next(iterator))
    seq.append(a)
    if idx == 0:
        pfs=[a] # Prefix sum
        pfssquared=[a**2]
    else:
        pfs.append(a+pfs[idx-1])
        pfssquared.append(a**2+pfssquared[idx-1])

result = 0
for i in range(0,n-1):
    s = pfssquared[i]*(pfs[n-1]-pfs[i])
    if s > result:
        result = s

print(result)