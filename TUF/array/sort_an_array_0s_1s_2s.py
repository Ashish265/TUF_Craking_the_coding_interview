"""
Problem Statement: Given an array consisting of only 0s, 1s, and 2s. 
Write a program to in-place sort the array without using inbuilt sort functions. 
( Expected: Single pass-O(N) and constant space)

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Input: nums = [0]
Output: [0]


"""

def sort_array(arr):

    low = 0
    mid = 0
    high = len(arr)-1

    while mid <= high:

        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low +1
            mid = mid +1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage:
# 
arr = [2,0,2,1,1,0]
print(sort_array(arr))  # Output: [0,0,1,1,2,2]