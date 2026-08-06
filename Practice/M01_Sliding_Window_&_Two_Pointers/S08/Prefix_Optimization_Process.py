'''
#LeetCode 1480. Running Sum of 1d Array
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
'''
nums = [1, 2, 3, 4]
res = [0] * len(nums)   #O(n) 
for i in range(len(nums)):
    curr_sum = 0
    for j in range(i + 1):    #O(n*2)
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)

#Optimal Solution 
nums = [1, 2, 3, 4]
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]   #O(n)
print(nums)
