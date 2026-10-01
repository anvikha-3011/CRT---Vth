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
            return "Queue is empty"
        return self.q.pop(0) 
    
    def front(self):
        if not self.is_empty():
            return "Queue is empty"
        return self.q[0]

    def display(self):
        if self.is_empty():
            return "Queue is empty"
        for ele in self.q:
            print(ele, end=" ")

q = Queue()
print(q.is_empty())  # True
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  # [10, 20, 30]


