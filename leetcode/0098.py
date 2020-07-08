# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, maxVal=None, minVal=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        if maxVal is not None and root.val > maxVal:
            return False
        if minVal is not None and root.val < minVal:
            return False
        
        return self.isValidBST(root.left, minVal=minVal, maxVal=root.val-1) and \
               self.isValidBST(root.right, minVal=root.val+1, maxVal=maxVal)
        
