from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_binary_tree_alternating(root):
    """ 
    Print the data contained in a binary tree layer by layer,
    left to right if the layer is even and right to left if the layer is odd
    """

    if root is None:
        return

    ilevel = 0
    stacks = [[root]]
    while len(stacks[-1]) > 0:
        
        # if current level stack is empty, move to the next level
        if len(stacks[ilevel]) == 0:
            ilevel += 1
            
        
        node = stacks[ilevel].pop()

        print(node.val)

        # if even, we are moving from left to right (since it is a stack, they will then be read right to left)
        if ilevel % 2 == 0:
            first, second = node.left, node.right
        else:
            first, second = node.right, node.left

        # add queue for following level if it does not yet exist
        if (first or second) and len(stacks) == ilevel+1:
            stacks.append([])

        if first:
            stacks[ilevel+1].append(first)
        if second:
            stacks[ilevel+1].append(second)


if __name__ == "__main__":
    print_binary_tree_alternating(
        TreeNode(0, 
                 TreeNode(1, None, TreeNode(2)), 
                 TreeNode(3, TreeNode(4, TreeNode(6)), TreeNode(5, None, TreeNode(7)))
             )
    )
            
