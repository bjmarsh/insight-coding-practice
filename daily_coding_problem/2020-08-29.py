"""
Given the root to a binary search tree, find the second largest node in the tree.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self, level=0, pref='*'):
        if self.val is None:
            return "Empty tree"
        s = " "*2*level + pref + ' ' + str(self.val) + '\n'
        if self.left is not None:
            s += self.left.__repr__(level=level+1, pref='<')
        if self.right is not None:
            s += self.right.__repr__(level=level+1, pref='>')
        return s
        

class BinarySearchTree:
    def __init__(self, vals=None):
        if vals is None or len(vals) == 0:
            self.head = None
        else:
            self.head = TreeNode(vals[0])
            for x in vals[1:]:
                self.insert(x)

    def insert(self, x):
        if self.head is None:
            self.head = TreeNode(x)
            return

        prev = None
        node = self.head
        while node is not None:
            prev = node
            if x < node.val:
                node = node.left
            else:
                node = node.right

        if x < prev.val:
            prev.left = TreeNode(x)
        else:
            prev.right = TreeNode(x)


    def __repr__(self):
        return repr(self.head)

def get_largest(bst):
    if isinstance(bst, BinarySearchTree):
        return get_largest(bst.head)

    prev = None
    node = bst
    while node is not None:
        prev = node
        node = node.right
    return prev.val


def get_second_largest(bst):
    if isinstance(bst, BinarySearchTree):
        return get_second_largest(bst.head)

    if bst is None:
        return None
    
    if bst.left is None and bst.right is None:
        return None
    
    if bst.right is None:
        return get_largest(bst.left)

    right_2nd_largest = get_second_largest(bst.right)
    if right_2nd_largest is not None:
        return right_2nd_largest

    return bst.val

if __name__ == "__main__":
    import random
    vals = [random.randint(0,999) for i in range(40)]
    bst = BinarySearchTree(vals)
    print(bst)
    print(sorted(vals)[-2])
    print(get_second_largest(bst))
