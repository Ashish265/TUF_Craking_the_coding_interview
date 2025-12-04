"""
Docstring for TUF.array.subarray_with_given_sum

Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.
 A subarray is a contiguous non-empty sequence of elements within an array.

Input : N = 4, array[] = {3, 1, 2, 4}, k = 6
Output: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

Input: N = 3, array[] = {1,2,3}, k = 3
Output: 2
Explanation: The subarrays that sum up to 3 are [1, 2], and [3].

"""

def subarray_with_given_sum(arr, k):

    n = len(arr)

    prefix_sum_count = {0: 1}  # Initialize with sum 0 occurring once
    prefix_sum= 0
    count = 0

    for i in range(n):

        prefix_sum += arr[i]

        remove = prefix_sum - k

        if remove in prefix_sum_count:
            count += prefix_sum_count[remove]

        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

    return count

# Example usage
arr1 = [3, 1, 2, 4]
k1 = 6
print(subarray_with_given_sum(arr1, k1))  # Output: 2       

arr2 = [1, 2, 3]
k2 = 3
print(subarray_with_given_sum(arr2, k2))  # Output: 2   