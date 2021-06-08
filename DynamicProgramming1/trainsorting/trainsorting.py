n = int(input())
if n == 0:
    print(0)
    exit()

# Input
train_carts = []
for x in range(0,n):
    train_carts.append(int(input()))
train_carts.reverse()

# Longest Increasing/Decreasing Subsequence
inc = [1]*n
dec = [1]*n

for i in range (1,n): 
    for j in range(0,i): 
        if  inc[i] < inc[j]+1 and train_carts[i] > train_carts[j]: 
            inc[i] = inc[j]+1
        if  dec[i] < dec[j]+1 and train_carts[i] < train_carts[j]: 
            dec[i] = dec[j]+1


res=0
for i in range(0,n): 
    res = max((inc[i] + dec[i]), res)

print(res-1)