"""
Docstring for TUF.binary_search.binary_search_on_answer.n_th__root_of_number
Problem Statement: Given two numbers N and M, find the Nth root of M.
The nth root of a number M is defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.

Input: N = 3, M = 27
Output: 3
Explanation: The cube root of 27 is equal to 3.
Input : N = 4, M = 69
Output: -1
Explanation : The 4th root of 69 does not exist. So, the answer is -1.

"""

def nth_root_bs(n, m):
    if m == 0 or  m == 1:
        return m
    low, high = 0, m
    ans = -1

    while low <= high:

        mid = (low +high) //2
        mid_pow = mid ** n
        if mid_pow == m:
            return mid
        elif mid_pow < m:
            low = mid + 1
        else:
            high = mid - 1
    return ans

# Driver code
if __name__ == "__main__":
    n = 3
    m = 27
    ans = nth_root_bs(n, m)
    print("The", n, "th root of", m, "is:", ans)

    n = 4
    m = 69
    ans = nth_root_bs(n, m)
    print("The", n, "th root of", m, "is:", ans)  