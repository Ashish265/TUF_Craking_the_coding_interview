"""
Docstring for TUF.binary_search.search_insert_position

Problem Statement: You are given a sorted array of distinct values and a target value x.
You need to search for the index of the target value in the array.

Example 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

Example 2:
Input Format: arr[] = {1,2,4,7}, x = 2
Result: 1
Explanation: 2 is present in the array and so we will return its index i.e. 1.

"""

def search_insert(arr, x):

    n = len(arr)
    low, high = 0, n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

# Example usage:
if __name__ == "__main__":
    arr1 = [1, 2, 4, 7]
    x1 = 6
    print(search_insert(arr1, x1))  # Output: 3

    arr2 = [1, 2, 4, 7]
    x2 = 2
    print(search_insert(arr2, x2))  # Output: 1

