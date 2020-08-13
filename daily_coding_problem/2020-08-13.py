"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def solution(headA: ListNode, headB: ListNode) -> ListNode:
    
    # O(m+n) time and O(m) space

    anodes = set()
    while headA is not None:
        anodes.add(headA)
        headA = headA.next
            
    while headB not in anodes and headB is not None:
        headB = headB.next
    
    return headB
    
if __name__ == "__main__":
    common = ListNode(8, ListNode(10))
    print(solution(
        ListNode(3, ListNode(7, common)),
        ListNode(99, ListNode(1, common))
        ).val
      )
