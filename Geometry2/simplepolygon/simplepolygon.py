import math as m

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = m.sqrt(self.x * self.x + self.y * self.y)
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __lt__(self, other):
        if self.x > other.x:
            return False
        if self.x == other.x:
            if self.y > other.y:
                return False
        return True
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def pointLine(current, prev1, prev2):
    v1 = Point(prev1.x - prev2.x, prev1.y - prev2.y)
    v2 = Point(current.x - prev2.x, current.y - prev2.y)

    return v1.x * v2.y - v1.y * v2.x

c = int(input())

for case in range(c):
    inp = [int(x) for x in input().split()]

    n = inp[0]

    cor = []

    for x in range(1,len(inp),2):
        cor.append(Point(inp[x],inp[x+1]))

    #print("cor",cor)
    
    points = sorted(cor)
    polygon = []

    #print(points)

    for i in range(len(points)):
        while len(polygon) >=2 and (pointLine(points[i], polygon[-1], polygon[-2]) > 0):
            polygon.pop()
  
        polygon.append(points[i])

    for i in range(len(points)-1,-1,-1):
        if points[i] not in polygon:
            polygon.append(points[i])
        
    #print(polygon)

    res = []
    for r in polygon:
        res.append(cor.index(r))

    print(*res)