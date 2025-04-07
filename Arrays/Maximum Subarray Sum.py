T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, N):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
     
    print(max_sum)

