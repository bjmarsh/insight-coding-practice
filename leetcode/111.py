# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        if root is None:
            return 0
    
        queue = deque()
        queue.append((root,1))
        while len(queue)>0:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                queue.append((node.left, depth+1))
            if node.right is not None:
                queue.append((node.right, depth+1))
        
