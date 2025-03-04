t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    m=min(a)
    op = sum(1 for x in a if x > m)
    print(op)
    t -= 1

