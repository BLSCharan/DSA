n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    is_largest = True
    for j in range(i + 1, n):
        if arr[j] >= arr[i]:
            is_largest = False
            break
    if is_largest:
        print(arr[i], end=" ")
print()

