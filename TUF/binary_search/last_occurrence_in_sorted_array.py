"""
Docstring for TUF.binary_search.last_occurrence_in_sorted_array
Problem Statement: Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key.
If the target is not found then return -1. Note: Consider 0 based indexing

Example 1:  
Input: N = 7, target = 13, array[] = {3, 4, 13, 13, 13, 20, 40}  
Output: 4  
Explanation: The target value 13 appears for the first time at index number 2 in the array.  

Example 2:  
Input: N = 7, target = 60, array[] = {3, 4, 13, 13, 13, 20, 40}  
Output: -1  
Explanation: Target value 60 is not present in the array, so the output is -1.
"""


def last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1  # Move to the right half to find the last occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result

# Example usage
arr1 = [3, 4, 13, 13, 13, 20, 40]
target1 = 13
print(last_occurrence(arr1, target1))  # Output: 4  
arr2 = [3, 4, 13, 13, 13, 20, 40]
target2 = 60
print(last_occurrence(arr2, target2))  # Output: -1
