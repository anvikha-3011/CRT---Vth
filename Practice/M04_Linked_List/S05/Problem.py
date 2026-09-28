#Leetcode Problem 876: Middle of the Linked List
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0 
        temp = head 
        while temp:
            count += 1 
            temp = temp.next 
        mid_ind = count // 2
        temp = head 
        for i in range(mid_ind):
            temp = temp.next 
        return temp 

#LeetCode Problem 141: Linked List Cycle
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set() 
        temp = head 
        while temp: 
            if temp in visited:
                return True 
            visited.add(temp) 
            temp = temp.next 
        return False 
        