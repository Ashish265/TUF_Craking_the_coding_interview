"""
Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

Examples:

Example 1:
Input: arr[]= 1 2 3 4 5, num = 3
Output: 2
Explanation: 3 is present in the 2nd index

Example 2:
Input: arr[]= 5 4 3 2 1, num = 5
Output: 0
Explanation: 5 is present in the 0th index
"""

def linear_search(arr,num):
    n = len(arr)
    for i in range(n):
        if arr[i] == num:
            return i
    return -1

print("Element found at index:", linear_search([1, 2, 3, 4, 5], 3))
print("Element found at index:", linear_search([5, 4, 3, 2, 1], 5))
print("Element found at index:", linear_search([10, 20, 30, 40, 50], 25))  # Example where element is not present