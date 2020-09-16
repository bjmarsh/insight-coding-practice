
"""
Suppose an arithmetic expression is given as a binary tree. 
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def eval_tree(root):
    
    if root.left is None and root.right is None:
        return root.val
    elif root.left is None or root.right is None:
        raise Exception("invalid tree")

    if root.val not in "+-*/":
        raise Exception("invalid tree")

    lval = eval_tree(root.left)
    rval = eval_tree(root.right)

    return eval(str(lval)+root.val+str(rval))
    
    

if __name__ == "__main__":
    print(eval_tree(TreeNode('*', TreeNode('+', TreeNode(3), TreeNode(2)), TreeNode('+', TreeNode(4), TreeNode(5)))))


