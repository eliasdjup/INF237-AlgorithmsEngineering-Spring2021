class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"

class Line:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        super().__init__()

    def intersect(self, other):
        if self.p == self.q or other.p == other.q: 
            return False

        # Checking for colinearity
        d = ((self.q.x - self.p.x) * (other.q.y - other.p.y)) - ((self.q.y - self.p.y) * (other.q.x - other.p.x))
        
        if (d == 0): 
            return False

        # Checking whether the other line is to the left or right
        a = (((self.p.y - other.p.y) * (other.q.x - other.p.x)) - ((self.p.x - other.p.x) * (other.q.y - other.p.y))) / d
        b = (((self.p.y - other.p.y) * (self.q.x - self.p.x)) - ((self.p.x - other.p.x) * (self.q.y - self.p.y))) / d
        
        # If not colinear or to the left or right the lines intersect.
        return (a >= 0 and a <= 1) and (b >= 0 and b <= 1)
    
    def __repr__(self):
        return "("+str(self.p)+","+str(self.q)+")"

class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = []
        self.segments = []
    
    def __repr__(self):
        return "Graph:"+str(self.segments)

    def addLine(self, line):
        self.segments.append(line)
        self.edges.append(set())

        current =  len(self.segments) - 1
        for i in range(current):
            if (line.intersect(self.segments[i])):
                self.edges[current].add(i)
                self.edges[i].add(current)
    
    def nTriangles(self):
        res = set()
        # Traversing 3 by 3 all intersections
        for a in range(self.V):
            for b in self.edges[a]:
                for c in self.edges[b]:
                    if a in self.edges[c]:
                        res.add(Triangle(a,b,c))

        return len(res)

class Triangle:
    def __init__(self, x, y, z):
        # Sorting 3 points
        a1 = min(x, y, z)
        a3 = max(x, y, z)
        a2 = (x + y + z) - a1 - a3
        
        self.arr = [a1,a2,a3]

    def __eq__(self, other):
        return self.arr[0] == other.arr[0] and self.arr[1] == other.arr[1] and self.arr[2] == other.arr[2]

    def __hash__(self):
        return hash((self.arr[0],self.arr[1],self.arr[2]))

    def __repr__(self):
        return "("+str(self.arr[0]) +","+ str(self.arr[1]) + "," + str(self.arr[2])+")"


n = int(input())

while n != 0:
    G = Graph(n)

    for i in range (n):
        px, py, qx, qy = [float(x) for x in input().split()]
        G.addLine(Line(Point(px,py),Point(qx,qy)))

    print(G.nTriangles())
    
    n = int(input())

