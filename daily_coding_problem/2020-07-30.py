"""
An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, 
which is an XOR of the next node and the previous node. Implement an XOR linked list; 
it has an add(element) which adds the element to the end, 
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer 
functions that converts between nodes and memory addresses.
"""

class XORListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        next_addr = 0 if next is None else get_pointer(next)
        prev_addr = 0 if prev is None else get_pointer(prev)
        self.link = next_addr ^ prev_addr

class XORLinkedList:
    def __init__(self, head=None):
        self.head = head

    def get(self, index):
        """ Get the element at a specified index
            Raise an exception if index is out of bounds
        """
        if self.head is None:
            raise Exception("Index {0} is out of bounds for XORLinkedList of size 0".format(index))

        prev_addr = 0
        node = self.head
        for i in range(index):
            next_addr = node.link ^ prev_addr
            if next_addr == 0:
                raise Exception("Index {0} is out of bounds for XORLinkedList of size {1}".format(index, i+1))
            prev_addr = get_pointer(node)
            node = dereference_pointer(next_addr)

        return node.val

    def add(element):
        """ Add an element to the end of the list """

        if self.head is None:
            self.head = XORListNode(element)
            return

        prev_addr = 0
        next_addr = get_pointer(self.head)
        while next_addr != 0:
            node = dereference_pointer(next_addr)
            next_addr = node.link ^ prev_addr
            prev_addr = get_pointer(node)

        # prev_addr is now address of last element
        tail = dereference_pointer(prev_addr)
        new_node = XORListNode(element, prev=tail)
        tail.link ^= get_pointer(new_node)
            
