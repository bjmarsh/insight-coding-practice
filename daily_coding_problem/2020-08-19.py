"""
Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        node = self
        s = ""
        while node.next is not None:
            s += str(node.val) + " -> "
            node = node.next
        s += str(node.val)
        return s


def solution(head: ListNode, k: int) -> None:

    lead = head
    for i in range(k):
        lead = lead.next

    prev = None
    lag = head
    while lead.next is not None:
        prev = lag
        lag = lag.next
        lead = lead.next
    
    # lead points to last element
    # lag points to element we want to delete
    # prev points to element before lag

    if prev is not None:
        prev.next = lag.next
        return head
    else:
        return lag.next

if __name__ == "__main__":
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(ll)
    ll = solution(ll, 3)
    print(ll)

