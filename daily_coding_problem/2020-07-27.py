"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.
"""
from collections import deque
from ast import literal_eval

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: Node) -> str:
    """
    serialize a binary tree
    """
    if root is None:
        return '[]'
    tree = []
    queue = deque()
    queue.append(root)
    n_nonnull = 1
    while n_nonnull > 0:
        node = queue.popleft()
        if node is not None:
            tree.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
            n_nonnull += -1 + (1 if node.left else 0) + (1 if node.right else 0)
        else:
            tree.append(None)
            queue.append(None)
            queue.append(None)
    return str(tree)

def deserialize(serialized: str) -> Node:
    """
    deserialize a binary tree
    """
    tree = literal_eval(serialized)
    if len(tree) == 0:
        return None
    root = Node(tree[0])
    parents = deque()
    parents.append(root)
    i = 1
    while i < len(tree):
        parent = parents.popleft()
        if parent is None:
            parents.append(None)
            parents.append(None)
        else:
            if tree[i] is not None:
                parent.left = Node(tree[i])
            if i+1 < len(tree) and tree[i+1] is not None:
                parent.right = Node(tree[i+1])
            parents.append(parent.left)
            parents.append(parent.right)
        i += 2
    return root

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right', Node('right.left')))
    serialized = serialize(node)
    print(serialized)
    print(serialize(deserialize(serialized)))
    assert deserialize(serialized).left.left.val == 'left.left'

