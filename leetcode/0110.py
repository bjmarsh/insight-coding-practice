# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def height_balanced(self, root):
        """ return a 2-tuple (bool, int) (balanced, height)"""
        
        if root is None:
            return True, 0
        
        lbal, lheight = self.height_balanced(root.left)
        rbal, rheight = self.height_balanced(root.right)
        
        height = 1 + max(lheight, rheight)
        bal = lbal and rbal and abs(lheight-rheight) <= 1

        return bal, height
        
    
    def isBalanced(self, root: TreeNode) -> bool:
        
        bal, height = self.height_balanced(root)
        # print(bal,height)
        return bal
