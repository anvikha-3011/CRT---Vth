#LeetCode 1763: Longest Nice Substring
from typing import List
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            char_set = set(sub)
            for c in char_set:
                if c.swapcase() not in char_set:
                    return False
            return True
        
        max_len = 0
        result = ""
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if is_nice(sub) and len(sub) > max_len:
                    max_len = len(sub)
                    result = sub
        
        return result
#LeetCode 1652: Defuse the Bomb
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        result = [0] * n
        
        for i in range(n):
            if k > 0:
                for j in range(1, k + 1):
                    result[i] += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    result[i] += code[(i - j) % n]
        
        return result