"""
Understanding recursion by priting a string multiple times
"""

def print_n_times(string, n):
    if n<=0:
        return
    print(string)
    print_n_times(string, n-1)

print_n_times("Hello", 5)