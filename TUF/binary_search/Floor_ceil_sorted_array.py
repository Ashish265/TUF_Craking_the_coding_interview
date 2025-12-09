"""
Docstring for TUF.binary_search.Floor_ceil_sorted_array

Problem Statement: You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
 The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x


Example 1:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

Example 2:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 8
Result: 8 8
Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.
"""

def floor_ceil(arr, x):
    n = len(arr)
    low, high = 0, n - 1
    floor, ceil = -1, -1

    # Finding floor
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] <= x:
            floor = arr[mid]
            low = mid + 1
        else:
            high = mid - 1

    # Resetting low and high for ceiling search
    low, high = 0, n - 1

    # Finding ceiling
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

    return floor, ceil


# Example usage:
if __name__ == "__main__":
    arr1 = [3, 4, 4, 7, 8, 10]
    x1 = 5
    print(floor_ceil(arr1, x1))  # Output: (4, 7)

    arr2 = [3, 4, 4, 7, 8, 10]
    x2 = 8
    print(floor_ceil(arr2, x2))  # Output: (8, 8)