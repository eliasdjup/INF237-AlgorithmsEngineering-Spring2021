# Time Limit Exceeded

import itertools
from collections import Counter

def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i


n_factors_A = int(input())
factors_A = map(int, input().split())

n_factors_B = int(input())
factors_B = map(int, input().split())

all_factors_A = Counter(list(itertools.chain.from_iterable(map(list,(map(prime_factors, factors_A))))))
all_factors_B = Counter(list(itertools.chain.from_iterable(map(list,(map(prime_factors, factors_B))))))
res = 1
for i in set(all_factors_A.keys()).intersection(set(all_factors_B.keys())):

    n = min(all_factors_A[i], all_factors_B[i])
    res *= i**n

print(str(res)[-9:])