t = int(input())
for _ in range(t):
    n = int(input()) 
    s = input().strip()
    op = 0 
    for i in range(n - 1):
        if s[i] == s[i + 1]: 
            op+= 1
    
    print(op)

