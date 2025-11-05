"""
Problem Statement: "Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.

Examples:

Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.

"""

def palindrome(s, i):
    n = len(s)
    if i >= n//2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return palindrome(s, i+1)


print(palindrome("ABCDCBA", 0))
print(palindrome("TAKE U FORWARD", 0))