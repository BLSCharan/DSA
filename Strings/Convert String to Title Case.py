T = int(input())

for _ in range(T):
    S = input().strip()
    words = S.split()
    result = []

    for word in words:
        if word.isupper():  
            result.append(word)
        else:
            result.append(word.capitalize())

    print(" ".join(result))  

