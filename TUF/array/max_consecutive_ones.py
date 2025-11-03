"""
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

Examples:

Example 1:

Input: prices = {1, 1, 0, 1, 1, 1}

Output: 3

Explanation: There are two consecutive 1's and three consecutive 1's in the array out of which maximum is 3.

Input: prices = {1, 0, 1, 1, 0, 1} 

Output: 2

Explanation: There are two consecutive 1's in the array.
"""

def max_consecutive(arr):
    n = len(arr)
    
    max_count = 0
    count = 0
    
    for i in range(n):
        if arr[i] == 1:
            count += 1
        else:
            
            count = 0
            
        max_count = max(count,max_count)
        
    return (max_count)


print("Maximum consecutive ones are:", max_consecutive([1, 1, 0, 1, 1, 1]))
print("Maximum consecutive ones are:", max_consecutive([1, 0, 1, 1, 0, 1]))