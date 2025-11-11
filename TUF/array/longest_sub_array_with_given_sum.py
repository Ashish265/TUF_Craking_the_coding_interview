"""
Longest Subarray with given Sum K(Positives)

Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
Result: 3
Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.

"""

def longest_subarray_with_sum_k(arr, k):
    max_length = 0
    current_sum = 0
    left = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        if current_sum == k:
            max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
# 
arr = [2, 3, 5, 1, 9]
k = 10
print(longest_subarray_with_sum_k(arr, k))  # Output: 3            