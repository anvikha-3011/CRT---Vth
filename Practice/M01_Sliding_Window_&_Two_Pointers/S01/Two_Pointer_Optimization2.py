'''
#LeetCode Problem: 26 Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1 
                nums[i] = nums[j]
        return i+1
'''
'''
#LeetCode Problem: 27 Remove Element 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
'''
'''
#LeetCode Problem: 283 Move Zeroes
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        while k < len(nums):
            nums[k] = 0
            k += 1
'''
'''
#LeetCode Problem: 167 Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left,right = 0,n-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1,right+1]
            elif s > target:
                right -= 1
            else:
                left += 1
'''

