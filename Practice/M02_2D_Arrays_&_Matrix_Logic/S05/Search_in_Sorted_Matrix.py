#LeetCode: 74. Search a 2D Matrix
from ast import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    arr = [] 
    for row in matrix:
        arr += row 
    n = len(arr) 
    left,right = 0,n-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))
