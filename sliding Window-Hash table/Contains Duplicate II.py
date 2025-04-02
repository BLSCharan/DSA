class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        h={}
        for i in range(len(nums)):
            if nums[i] in h and abs(i-h[nums[i]])<=k:
                return True
            h[nums[i]]=i
        return False
 
