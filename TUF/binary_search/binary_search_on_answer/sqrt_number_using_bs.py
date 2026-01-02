"""
Docstring for TUF.binary_search.binary_search_on_answer.sqrt_number_using_bs
Finding Sqrt of a number using Binary Search
Input: N = 36
Output: 6
Explanation: Square root of 36 is 6. 
Input: N = 28
Output: 5
Explanation: Square root of 28 is approximately 5.292. So, the floor value will be 5. 
"""

def sqrt_bs(n):
    if n == 0 or n == 1:
        return n
    
    low, high = 1, n
    ans = 0

    while low <= high:
        mide = ( low + high)//2
        midsq = mide * mide 
        if midsq == n:
            return mide
        elif midsq < n:
            ans = mide
            low = mide + 1
        else:
            high = mide - 1
    return ans


# Driver code
if __name__ == "__main__":
    n = 28
    ans = sqrt_bs(n)
    print("The square root of", n, "is:", ans)

    n = 36
    ans = sqrt_bs(n)
    print("The square root of", n, "is:", ans)  