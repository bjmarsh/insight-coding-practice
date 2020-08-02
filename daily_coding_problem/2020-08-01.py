"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def n_unival_subtrees(root: TreeNode) -> int:
    
    def helper(root):
        """
        Return two values: the number of unival subtrees,
        and a boolean indicating whether or not the entire tree is unival
        """
        if root is None:
            return 0, True

        left_n, left_isUnival = helper(root.left)
        right_n, right_isUnival = helper(root.right)

        n = left_n + right_n
        isUnival = False
        if (root.left is None and root.right is None) or \
           (root.left is None and right_isUnival and root.val == root.right.val) or \
           (root.right is None and left_isUnival and root.val == root.left.val) or \
           (right_isUnival and left_isUnival and root.val == root.right.val and root.val == root.left.val):
            isUnival = True
            n += 1

        return n, isUnival
        
    return helper(root)[0]

if __name__ == "__main__":
    root = TreeNode(0, TreeNode(1), TreeNode(0, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(0)))
    print(n_unival_subtrees(root))


