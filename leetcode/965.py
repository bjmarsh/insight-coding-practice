# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
    
        return (root.left is None or root.left.val==root.val and self.isUnivalTree(root.left)) and \
               (root.right is None or root.right.val==root.val and self.isUnivalTree(root.right)) 

