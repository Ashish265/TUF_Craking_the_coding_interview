"""
Docstring for TUF.binary_search.binary_search_on_answer.minimum_days_to_make_n_bouquets

Problem Statement: You are given 'N’ roses and you are also given an array 'arr' where 'arr[i]' denotes that the 'ith' rose will bloom on the 'arr[i]th' day. You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet. Find the minimum number of days required to make at least ‘m' bouquets each containing 'k' roses.
 Return -1 if it is not possible.
 Example 1:
Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
Result: 12
Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

Example 2:
Input Format: N = 5, arr[] = {1, 10, 3, 10, 2}, m = 3, k = 2
Result: -1
Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers. But we are given only 5 flowers, so, we cannot make the bouquets.

"""

def can_make_bouquets(arr, days, m, k):
    bouquets = 0
    flowers = 0

    for bloom_day in arr:
        if bloom_day <= days:
            flowers += 1
            if flowers == k:
                bouquets += 1
                flowers = 0
        else:
            flowers = 0

    return bouquets >= m 

def min_days_to_make_bouquets(arr, m, k):
    if m * k > len(arr):
        return -1

    left, right = 1, max(arr)
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if can_make_bouquets(arr, mid, m, k):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Example usage:
if __name__ == "__main__": 
    arr = [7, 7, 7, 7, 13, 11, 12, 7]
    m = 2
    k = 3
    print(min_days_to_make_bouquets(arr, m, k))  # Output: 12

    arr = [1, 10, 3, 10, 2]
    m = 3
    k = 2
    print(min_days_to_make_bouquets(arr, m, k))  # Output: -1

    arr = [1, 2, 4, 9, 3, 4, 1]
    m = 2
    k = 3
    print(min_days_to_make_bouquets(arr, m, k))  # Output: 4
    arr = [5, 5, 5, 5, 5]
    m = 1
    k = 5
    print(min_days_to_make_bouquets(arr, m, k))  # Output: 5