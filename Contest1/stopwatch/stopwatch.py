N = int(input())


if (N % 2) != 0:
    print("still running")
    exit()

lst = []
for i in range(N):
    lst.append(int(input()))


res = 0

for i in range(0,len(lst)-1,2):
    res = res + ((lst[i+1])-(lst[i]))

print(res)

