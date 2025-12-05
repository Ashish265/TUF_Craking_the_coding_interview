"""
Docstring for TUF.binary_search.binary_search

Problem statement: You are given a sorted array of integers and a target, your task is to search for the target in the given array. 
Assume the given array does not contain any duplicate numbers.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

# Example usage
arr1 = [1, 2, 3, 4, 5, 6]
target1 = 4
print(binary_search(arr1, target1))  # Output: 3    
arr2 = [10, 20, 30, 40, 50]
target2 = 25
print(binary_search(arr2, target2))  # Output: -1