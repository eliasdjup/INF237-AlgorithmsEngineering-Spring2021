import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    
    def center(self, other, radius):
        mid = Point(((self.x + other.x)/2), ((self.y + other.y)/2))
        l = (math.pow(radius, 2)) - (math.pow(self.dist(mid), 2))

        # Square root of zero
        if l < 0:
            return None

        mid_centre = math.sqrt(l)

        # Theta from polar coordinates
        radians = math.atan2(self.x - other.x, other.y - self.y) #Here i did the mistake of taking self.y - other.y, which does not give the middle point

        return Point(mid_centre * math.cos(radians) + mid.x, mid_centre * math.sin(radians) + mid.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

n = int(input())

for _ in range(n):
    input()
    inp = input().split()
    m = int(inp[0])
    r = float(inp[1])/2.0 # Took me a long time debugging to find out input is diameter, not radius

    points = []

    for _ in range(m):
        x, y = [float(x) for x in input().split()]
        points.append(Point(x,y))

    res = 0

    for a in range(m):
        for b in range(m):
            temp_res = 0

            cntr = points[a].center(points[b],r)

            if cntr is None:
                continue

            for c in range(m):
                p_dist = cntr.dist(points[c])
                if (p_dist <= r):
                    temp_res += 1
 
            if (temp_res > res): 
                res = temp_res

    print(res)