"""
Docstring for TUF.binary_search.num_times_array_rotated

Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values).
Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated.

Input : arr = [4,5,6,7,0,1,2,3]
Result: 4
Explanation: The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.

Input : arr = [3,4,5,1,2]
Output : 3
Explanation: The original array should be [1,2,3,4,5]. So, we can notice that the array has been rotated 3 times.
"""

def findRotations(nums):
    low, high = 0 , len(nums) - 1

    while low < high:

        mid = low + (high - low)// 2

        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

        return low
    
nums = [4,5,6,7,0,1,2]
print(findRotations(nums))