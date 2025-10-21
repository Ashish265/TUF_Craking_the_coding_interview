"""
Given an array of non-negative integers, arr,
return an array with the same length
where index i contains the product of all the elements in arr except arr[i].
Since the values could be very large, return them modulo 10^9 + 7.

Example 1:
arr = [1, 3, 2, 1]
Output: [6, 2, 3, 6]

Example 2:
arr = [0, 1, 0]
Output: [0, 0, 0]

"""

def product_except_self(arr):

    n = len(arr)

    prefix = [1]*n
    suffix = [1]*n

    
    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = prefix[i-1] * arr[i]

    
    suffix[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * arr[i]

    res = [1] * n
    res[0] = suffix[1]
    res[n-1] = prefix[n-2]

    for i in range(1,n-1):
        res[i] = prefix[i-1] * suffix[i+1]

    return res


arr = [1, 3, 2, 1]

print(product_except_self(arr))


