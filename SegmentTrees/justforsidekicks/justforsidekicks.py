# Binary indexed tree/ Fenwick tree
# The idea is based on the fact that all positive integers can be represented as the sum of powers of 2. 
# Every node of the BITree stores the sum of n elements where n is a power of 2. 
# The number of set bits in the binary representation of a number n is O(Logn). 
# Therefore, we traverse at-most O(Logn) nodes in both getSum() and update() operations. 
# The time complexity of the construction is O(nLogn) as it calls update() for all n elements.

class BIT:
    def __init__(self, size):     
        self.size = size
        self.tree = [0 for i in range(self.size+1)]
            
    def update(self, index, val):
        index = index+1
        while index <= self.size:
            self.tree[index] += val
            index += index & (-index)
    
    def getSum(self, index):
        s = 0
        index = index+1

        while index > 0:
            s += self.tree[index]
            index -= index & (-index) 

        return s

    def getSumRange(self,a,b):
        return self.getSum(b) - self.getSum(a-1)

    def __repr__(self):
        return ("BIT:"+str(self.tree))

    
n,q = [int(x) for x in input().split()]
gem_values = [int(x) for x in input().split()]
gems = [(int(x)) for x in input().split(sep=None)[0]]

print(gem_values)
print(gems)

trees=[]
for i in range(6):
    trees.append(BIT(n+1))

for i in range(0,n):
    trees[gems[i]-1].update(i,1)

for _ in range(q):
    i, a, b = [int(x) for x in input().split()]

    if i == 1:
        trees[gems[a-1]-1].update(a-1, -1)
        gems[a-1] = b
        trees[gems[a-1]-1].update(a-1, 1)

    elif i == 2:
        gem_values[a-1] = b
    
    else:
        res = 0
        for j in range(0,6):
            res += (trees[j].getSumRange(a-1, b-1)) * gem_values[j]
        print(res)