# Time Limit Exceeded
N = int(input())

def pref(x,lst):
    return(lst.append(x+lst[-1]))

x = []

y = []
ypref=[0]


for i in range(N):
    inp = [int(x) for x in input().split()]
    x.append(inp[0])
    y.append(inp[1])

x.sort()
y.sort()

print(x,y)