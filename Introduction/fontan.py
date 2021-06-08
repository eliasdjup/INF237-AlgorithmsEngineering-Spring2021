ylen,xlen = map(int, input().split())

l = []
startWater= []
for y in range(ylen):
    t = [i for i in input().split()[0]]
    for x in range(xlen):
        if t[x] == 'V':
            startWater.append((y,x))
    l.append(t)

def recWater(y,x):
    if (y+1 > ylen-1):
        return

    below = l[y+1][x]

    if (below == 'V'):

        return
    if (below == '.'):
        l[y+1][x] = 'V'
        recWater(y+1,x)


    if (below == '#'):
        #right
        if (x+1<xlen):
            if (l[y][x+1] == '.'):
                l[y][x+1] = 'V'
                recWater(y,x+1)
        #left
        if (x-1>= 0):
            if (l[y][x-1] == '.'):
                l[y][x-1] = 'V'
                recWater(y,x-1)   

for (a,b) in startWater:
    recWater(a,b)

for i in l:
    print(''.join(i))