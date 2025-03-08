t=int(input())
for i in range(t):
    s=input()
    t=input()
    m=[]
    for i in range(len(s)):
        if s[i]==t[i]:
            m.append("G")
        else:
            m.append("B")
    print("".join(m))
