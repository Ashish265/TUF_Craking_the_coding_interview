"""
Docstring for TUF.binary_search.min_rotated_sorted_array

Input: arr = [4,5,6,7,0,1,2,3]
Output: 0
Explanation: The minimum element in the array is 0.
Input : arr = [3,4,5,1,2]
Output: 1
Explanation : The minimum element in the array is 1.

"""


def findMin(nums):

    low,high = 0, len(nums)-1
    while low < high:
        mid = low + (high - low) // 2

        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid 
    return nums[low]


nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))