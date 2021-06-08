fac = [1] * 50
for i in range(2, 50):
    fac[i] = i * fac[i-1]

while True:
    try:
        n, k = [int(x) for x in input().split()]
        nums = list(range(1,n+1))
        p = []
        while n > 0:
            n -= 1
            q = k // fac[n]
            p.append(nums[q])
            nums.pop(q)
            k %= fac[n]
        print(*p)
    except EOFError:
        exit()