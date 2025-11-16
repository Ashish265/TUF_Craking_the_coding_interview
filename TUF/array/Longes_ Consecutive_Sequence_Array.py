"""
Longest Consecutive Sequence in an Array

Problem Statement: You are given an array of 'N' integers. 
You need to find the length of the longest sequence which contains the consecutive elements.

Example 1:

Input: [100, 200, 1, 3, 2, 4]

Output: 4

Explanation: The longest consecutive subsequence is 1, 2, 3, and 4.

Input: [3, 8, 5, 7, 6]

Output: 4

Explanation: The longest consecutive subsequence is 5, 6, 7, and 8.
"""

def longest_consecutive_sequence(arr):

    n = len(arr)

    if n == 0:
        return 0
    
    st = set(arr)

    count = 0
    longest = 0

    for num in st:
        if num - 1 not in st:
            count = 1
            current_num = num

            while current_num + 1 in st:
                count += 1
                current_num += 1

            longest = max(longest, count)
    return longest

# Example usage
arr = [100, 200, 1, 3, 2, 4]
print(longest_consecutive_sequence(arr))  # Output: 4
