"""
Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

Examples:

Example 1:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Example 2:
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15
"""

def sum_n(n):
    if  n <= 0:
        return 0
    return n +sum_n(n-1)

print(sum_n(5))  # Output: 15