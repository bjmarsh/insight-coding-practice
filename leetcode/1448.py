# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, seen=[]) -> int:
        
        if root is None:
            return 0
        
        ngood = 0
        if len(seen)==0 or root.val >= max(seen):
            ngood += 1
            
        ngood += self.goodNodes(root.left, seen=seen+[root.val])
        ngood += self.goodNodes(root.right, seen=seen+[root.val])
        
        return ngood
