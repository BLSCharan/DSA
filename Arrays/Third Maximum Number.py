class Solution(object):
    def thirdMax(self, nums):
        nums=set(nums)
        if len(nums)>=3:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
        else:
            return max(nums)
