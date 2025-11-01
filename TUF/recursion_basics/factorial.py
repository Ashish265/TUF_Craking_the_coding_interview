"""
Problem Statement: Given a number X,  print its factorial.

To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.

Note: X  is always a positive number. 
"""

def factorial(n):
    if n == 0 or n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120