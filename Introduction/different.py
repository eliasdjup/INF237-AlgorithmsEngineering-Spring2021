import sys

for l in sys.stdin:
    a, b = map(int, l.split())
    print(abs(a-b))
sys.exit()

