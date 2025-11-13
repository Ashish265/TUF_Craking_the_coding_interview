"""
Rearrange Array Elements by Sign
Problem Statement:

There's an array 'A' of size 'N' with an equal number of positive and negative elements. 
Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Note: Start the array with positive elements.

Examples: 

Example 1:

Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5

"""

def arrange_array(arr):

    n = len(arr)
    ans = [0] * n

    pos_index= 0
    neg_index= 1

    for i in range(n):
        if arr[i] >= 0:
            ans[pos_index] = arr[i]
            pos_index += 2
        else:
            ans[neg_index] = arr[i]
            neg_index += 2

    return ans

print(arrange_array([1, 2, -4, -5]))  # Output: [1, -4, 2, -5]

