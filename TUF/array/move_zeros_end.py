"""
Problem Statement: You are given an array of integers, 
your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

Input : 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
Explanation : All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
"""
def move_zeros_end(arr):
    n = len(arr)
    i = 0
    j = n-1 

    while i < j:
        if arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] != 0:
            i += 1
        else:
            j -= 1
    return arr

print("Array after moving zeros to the end:", move_zeros_end([1, 0, 2, 3, 0, 4, 0, 1]))
print("Array after moving zeros to the end:", move_zeros_end([1, 2, 0, 1, 0, 4, 0]))
