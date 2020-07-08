# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return True

#         # O(n) time and O(n) space
#         x = [head.val]
#         while head.next is not None:
#             head = head.next
#             x.append(head.val)
#         return x==x[::-1]
    
        # O(n) time and O(1) space
    
        #first pass to determine number of elements:
        node = head
        N = 0
        while node is not None:
            N += 1
            node = node.next

        if N < 2:
            return True

        n_to_compare = N//2
        
        node = head
        prev = None
        for i in range(n_to_compare):
            prev = node
            node = node.next

        # reverse the second half of the list
        for i in range(n_to_compare, N):
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        # node should be None, and prev should be the final list element
        node1 = head
        node2 = prev
        for i in range(n_to_compare):
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True
