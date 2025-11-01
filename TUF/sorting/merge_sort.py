"""
Given an array of integers, nums,sort the array in non-decreasing order using the merge sort algorithm. Return the sorted array.



A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.


Examples:
Input: nums = [7, 4, 1, 5, 3]

Output: [1, 3, 4, 5, 7]

Explanation: 1 <= 3 <= 4 <= 5 <= 7.

Thus the array is sorted in non-decreasing order.

Input: nums = [5, 4, 4, 1, 1]

Output: [1, 1, 4, 4, 5]

Explanation: 1 <= 1 <= 4 <= 4 <= 5.

Thus the array is sorted in non-decreasing order
"""

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_half = merge_sort(nums[mid:])
    right_half = merge_sort(nums[:mid])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted_array.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_array.append(right[right_index])
        right_index += 1

    return sorted_array


print(merge_sort([7, 4, 1, 5, 3]))  # Output: [1, 3, 4, 5, 7]

    