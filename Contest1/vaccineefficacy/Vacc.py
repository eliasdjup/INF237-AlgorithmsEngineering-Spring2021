def toInt(c):
    if c == 'Y': return 1.0
    else: return 0.0

def eff(X,Y):
    Xres = sum(X)/len(X)
    Yres = sum(Y)/len(Y)

    if Xres < Yres:
        print((abs(Xres - Yres) / Yres) * 100.0)
    else:
        print("Not Effective")


N = int(input())

AVac = []
BVac = []
CVac = []

APlac = []
BPlac = []
CPlac = []

for i in range(N):
    lst = [x for x in input().split()[0]]

    if lst[0] == 'Y':
        AVac.append(toInt(lst[1]))
        BVac.append(toInt(lst[2]))
        CVac.append(toInt(lst[3]))
    
    else:
        APlac.append(toInt(lst[1]))
        BPlac.append(toInt(lst[2]))
        CPlac.append(toInt(lst[3]))


eff(AVac,APlac)
eff(BVac,BPlac)
eff(CVac,CPlac)