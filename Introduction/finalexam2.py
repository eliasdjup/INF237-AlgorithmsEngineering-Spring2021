q = int(input())

store = None
res = 0

for i in range(q):
    inp = input()
    if (inp == store):
        res+=1
    store = inp

print(res)

