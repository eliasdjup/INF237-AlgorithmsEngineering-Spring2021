# Time Limit Exceeded

n = int(input())


def path(x,y):

    maxX = x-1
    maxY = y-1

    corners = [(maxX,maxY), (maxX,0), (maxY,0)]

    currX = 0
    currY = 0

    path = set()

    path.add((0,0))

    d = "NE"

    while (currX, currY) not in corners:
        #print(currX,currY, d)

        if d == "SE":
            if (currX == maxX):
                d = "SW"
                currX-=1
                currY-=1
                path.add((currX,currY))
                continue
            if (currY == 0):
                d = "NE"
                currX+=1
                currY+=1
                path.add((currX,currY))
                continue

            currX += 1
            currY -= 1
            path.add((currX,currY))
        
        elif d == "SW":
            if (currY == 0):
                d = "NW"
                currX-=1
                currY+=1
                path.add((currX,currY))
                continue
            if (currX == 0):
                d = "SE"
                currX+=1
                currY-=1
                path.add((currX,currY))
                continue

            currX -= 1
            currY -= 1
            path.add((currX,currY))
        
        elif d == "NE":
            if (currY == maxY):
                d = "SE"
                currX+=1
                currY-=1
                path.add((currX,currY))
                continue
            if (currX == maxX):
                d = "NW"
                currX-=1
                currY+=1
                path.add((currX,currY))
                continue

            currX += 1
            currY += 1
            path.add((currX,currY))

        else: #NW
            if (currY == maxY):
                d = "SW"
                currX-=1
                currY-=1
                path.add((currX,currY))
                continue
            if (currX == 0):
                d = "NE"
                currX+=1
                currY+=1
                path.add((currX,currY))
                continue

            currX -= 1
            currY += 1
            path.add((currX,currY))
    
    print(len(path))


for i in range(n):
    x, y = [int(x) for x in input().split()]

    path(x,y)



