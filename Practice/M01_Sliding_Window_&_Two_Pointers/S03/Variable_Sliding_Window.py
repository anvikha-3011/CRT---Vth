
#LeetCode Problem 209: Minimum Size Subarray Sum
from ast import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        min_len = float("inf")
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right-left+1)
                cur_sum -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len 
    target = 7 
    nums = [2, 3, 1]

#LeetCode Problem 713: Subarray Product Less Than K
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        prod = 1
        count = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            count += right - left + 1
        return count
