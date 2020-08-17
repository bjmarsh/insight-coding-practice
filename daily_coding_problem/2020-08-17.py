"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

- is_locked, which returns whether the node is locked
- lock, which attempts to lock the node. If it cannot be locked, 
  then it should return false. Otherwise, it should lock it and return true.
- unlock, which unlocks the node. If it cannot be unlocked, then it should 
  return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. 
You may assume the class is used in a single-threaded program, so there is no need for 
actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""

class TreeNode:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

        self._is_locked = False
        self.n_locked_descendants = 0
        if left:
            self.n_locked_descentants += left.n_locked_descendants + left._is_locked
        if right:
            self.n_locked_descentants += right.n_locked_descendants + right._is_locked

        def is_locked(self):
            return self._is_locked

        def lock(self):
            if self._is_locked:
                return True
            if self.n_locked_descendants:
                return False

            node = self.parent
            while node is not None:
                if node._is_locked:
                    return False
                node = node.parent

            self._is_locked = True
            node = self.parent
            while node is not None:
                node.n_locked_descendants += 1
                node = node.parent

            return True

        def unlock(self):
            if not self._is_locked:
                return True
            if self.n_locked_descendants:
                return False

            node = self.parent
            while node is not None:
                if node._is_locked:
                    return False
                node = node.parent

            self._is_locked = False
            node = self.parent
            while node is not None:
                node.n_locked_descendants -= 1
                node = node.parent
            
            
