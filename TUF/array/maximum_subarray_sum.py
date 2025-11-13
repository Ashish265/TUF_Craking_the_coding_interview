"""
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Example 1:

Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

Output: 6 

Explanation: [4,-1,2,1] has the largest sum = 6. 

Examples 2: 

Input: arr = [1] 

Output: 1 

Explanation: Array has only one element and which is giving positive sum of 1. 

"""

def maximum_sub_array_sum_optimal(arr):
    n = len(arr)
    max_sum = float("-inf")
    current_sum=0

    for i in range(n):
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            
        if current_sum < 0:
            current_sum = 0
        
    return max_sum
    
print(maximum_sub_array_sum_optimal([-2,1,-3,4,-1,2,1,-5,4]))