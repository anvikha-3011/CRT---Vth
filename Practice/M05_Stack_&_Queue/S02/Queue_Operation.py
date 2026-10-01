#Implementation of a Queue using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        del_val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return del_val

    def front(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data

    def display(self):
        if self.front is None:
            return "Queue is empty"
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next