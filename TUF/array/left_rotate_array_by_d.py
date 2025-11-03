"""
Rotate array by K elements

Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

Examples:

Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.

"""

def left_rotate_k(arr, k):
    n = len(arr)

    if n == 0:
        return arr
    
    first_k_elements = arr[:k]

    for i in range(k, n):
        arr[i-k] = arr[i]

    arr[n-k:] = first_k_elements

    return arr

print("Array after left rotation by k elements:", left_rotate_k([1, 2, 3, 4, 5, 6, 7], 2))
print("Array after left rotation by k elements:", left_rotate_k([3, 7, 8, 9, 10, 11], 3))