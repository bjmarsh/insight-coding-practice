# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums, left=0, right=None):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if right is None:
            right = len(nums)-1
        
        if right-left < 0:
            return None
        
        if right==left:
            return TreeNode(nums[left])
        
        
        idx = (right+left)//2
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST(nums, left, idx-1)
        root.right = self.sortedArrayToBST(nums, idx+1, right)
            
        return root
        
