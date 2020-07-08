# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l2 is None:
            return l1
        if l1 is None:
            return l2
        
        if l2.val < l1.val:
            l1, l2 = l2, l1
        
        cur = l1
        cur1, cur2 = l1.next, l2
        while cur1 is not None or cur2 is not None:
            if cur2 is None or (cur1 is not None and cur1.val < cur2.val):
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        
        return l1
        
