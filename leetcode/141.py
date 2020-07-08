# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return False
        
        visited = {}
        while True:
            if head.val not in visited:
                visited[head.val] = []
            visited[head.val].append(head)
            head = head.next
            if head is None:
                return False
            if head in visited.get(head.val, []):
                return True
