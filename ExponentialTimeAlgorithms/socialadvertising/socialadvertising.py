# Spatial Resource Allocation
# Minimal dominant set

def graphSets(g, size, current, s, v, picked, num_nodes):
    if s == v:
        return True

    temp_set = g[current] | s

    if temp_set == v:
        return True
    
    if picked+1 == size:
        return False
        
    for next_node in range(current+1, num_nodes):
        if graphSets(g, size, next_node,temp_set,v, picked+1, num_nodes):
            return True
    
    return False

cases = int(input())
  
for c in range(cases):
    graph = dict([])
    num_nodes = int(input())

    graph = []
    for i in range(0,num_nodes):
        lst = [int(x) for x in input().split()]
        neigh = list(map(lambda x: x - 1, lst[1:]))

        bit_mask = ['0']*num_nodes
        bit_mask[i] = '1'

        for n in neigh:
            bit_mask[n] = '1'

        graph.append(int("".join(bit_mask),2))
    
    cont = True

    for size in range(1,num_nodes):
        if not cont:
            break
        for node in range(num_nodes):
            if not cont:
                break
            if graphSets(graph, size, node, 0, int('1'*num_nodes,2), 0, num_nodes):
                print(size)
                cont = False

    if cont == True:
        print(num_nodes)