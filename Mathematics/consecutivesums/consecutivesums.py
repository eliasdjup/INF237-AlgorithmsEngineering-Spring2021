def terms(n, i):
  mid = n // i
  d = (-i//2)+1
  t = []
  for x in range(i):
    t.append(mid + d)
    d += 1
  return t

T = int(input())

for case in range(T):
    n = int(input())
    if (n & (n-1) == 0) and (n != 0): # power of two
        print("IMPOSSIBLE")
    else:
        i = 2
        curr = -1
        while curr != n:
          t = terms(n, i)
          curr = sum(t)
          i += 1

        res = str(n)+" = "
        for i in range(len(t)):
          res += str(t[i])+ " + "

        print(res[:-3])