# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        n_ahead = head
        for i in range(n):
            n_ahead = n_ahead.next
        
        prev = None
        node = head
        while n_ahead is not None:
            prev = node
            node = node.next
            n_ahead = n_ahead.next
            
        if prev is None:
            return node.next
        else:
            prev.next = node.next
            return head
