class Solution(object):
    def moveZeroes(self, nums):
        position = 0
        for num in nums:
            if num != 0:  
                nums[position] = num  
                position += 1  

        for i in range(position, len(nums)):
            nums[i] = 0
