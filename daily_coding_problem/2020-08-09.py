"""
You run an e-commerce website and want to record the last N order IDs in a log. 
Implement a data structure to accomplish this, with the following API:
"""

class OrderLog:

    def __init__(self, N):
        self.ids = [None] * N
        self.cur_idx = 0 # index pointing to the next element to be filled

    def record(self, order_id):
        self.ids[cur_idx] = order_id
        self.cur_idx = (self.cur_idx + 1) % len(self.ids)

    def get_last(self, i):
        return self.ids[(self.cur_idx - i + len(self.ids)) % len(self.ids)]
