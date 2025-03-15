class Solution(object):
    def sortedArrayToBST(self, nums):
        tn=len(nums)
        if not tn:
            return None
        mid=tn//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid]) 
        root.right = self.sortedArrayToBST(nums[mid+1:]) 
        return root  
        
        
