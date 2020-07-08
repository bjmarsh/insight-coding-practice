# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_depth_diam(self, root):
        
        if root is None:
            return -1, 0
    
        ldepth, ldiam = self.get_depth_diam(root.left)
        rdepth, rdiam = self.get_depth_diam(root.right)
        
        return 1+max(ldepth, rdepth), max(ldiam, rdiam, 2+ldepth+rdepth)
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.get_depth_diam(root)[1]
        
