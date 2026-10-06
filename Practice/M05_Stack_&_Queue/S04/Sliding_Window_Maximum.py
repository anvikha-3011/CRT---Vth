#LeetCode - 901 - Online Stock Span
class StockSpanner:
    
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append((price, span))
        return span

#LeetCode - 239 - Sliding Window Maximum
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()  
        res = []
        
        for i, num in enumerate(nums):
            if q and q[0] <= i - k:
                q.popleft()
    
            while q and nums[q[-1]] <= num:
                q.pop()
                
            q.append(i)
            
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res

    