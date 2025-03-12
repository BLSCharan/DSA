class Solution(object):
    def maximumCount(self, nums):
        count=0
        neg=0
        for i in range(len(nums)):
            if nums[i]>=1:
                count+=1
            elif nums[i]<0:
                neg+=1
        return max(count,neg)
