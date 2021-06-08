# Time Limit Exceeded

from functools import reduce
from collections import Counter

n, h, l = map(int, input().split())
horror_list = list(map(int, input().split()))
horror_index = Counter()


same = []
for _ in range(l):
    a, b = map(int, input().split())
    if a in horror_list and b in horror_list:
        continue

    elif a in horror_list:
        horror_index[b] = 1

    elif b in horror_list:
        horror_index[a] = 1
    else:
        same.append((a, b))

while len(same) > 0:

    q = []
    for a, b in same:
        if a in horror_index or b in horror_index:
            q.append((a, b))

    for a, b in q:
        if a in horror_index and b in horror_index:

            if horror_index[a] > horror_index[b]:
                horror_index[b] = horror_index[a] + 1

            elif horror_index[a] < horror_index[b]:
                horror_index[a] = horror_index[b] + 1

        elif a in horror_index:
            horror_index[b] = horror_index[a] + 1

        elif b in horror_index:
            horror_index[a] = horror_index[b] + 1

        same.remove((a, b))
    
    if not q:
        break

if (len(same) > 0):
    print(min(map(min, same)))

else:
    minimum = 10000000000000
    for i,e in horror_index.items():
        if e == max(horror_index.values()):
            minimum = min(minimum, i)

    print(min([i for i, horror_list in horror_index.items() if horror_list == max(horror_index.values())]))