"""
Given an integer N, write a program to print numbers from 1 to N.
"""

def print_n(n):
    if n <= 0:
        return
    print_n(n-1)
    print(n)

print_n(5)
