"""
Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

Examples:

Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6

Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)"""

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibo(n-1) + fibo(n-2)

for i in range(10):
    print(fibo(i), end=" ")


    