#Queue Implementation using python list
class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, val):
        self.q.append(val)

    def is_empty(self):
        return len(self.q) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.q.pop(0)
        return None 