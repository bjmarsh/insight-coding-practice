"""
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) 
data structure with the following methods: enqueue, which inserts an element into the queue, 
and dequeue, which removes it.
"""

class Queue:
    def __init__(self):
        self.data = [] # a stack

    def enqueue(self, val):
        self.data.append(val) # push onto stack

    def dequeue(self):
        temp_stack = []
        while len(self.data) > 0:
            temp_stack.append(self.data.pop())
        val = temp_stack.pop()
        while len(temp_stack) > 0:
            self.data.append(temp_stack.pop())
        return val

if __name__ == "__main__":
    




