'''
#LeetCode Problem: 643 Maximum Average Subarray I
from ast import List
def findMaxAverage(nums: List[int], k: int) -> float:
    win_sum = sum(nums[:k])
    max_sum =win_sum
    n = len(nums)
    for i in range(0,n-k):
        win_sum = win_sum - nums[i] + nums[k+i]
        max_sum = max(win_sum,max_sum)
    return max_sum/k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))
'''
#LeetCode Problem: 1343 Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
from ast import List
