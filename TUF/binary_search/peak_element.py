"""
Docstring for TUF.binary_search.peak_element
Given an array of length N, peak element is defined as the element greater than both of its neighbors.
Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i]. 
Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.

Input: arr[] = {1,2,3,4,5,6,7,8,5,1}
Output: 7
Explanation: There is only 1 peak element, 8,  that is at index 7.
Input: arr[] = {1,2,1,3,5,6,4} 
Output: 1 
Explanation : There are 2 peak numbers that are at indices 1 and 5. We can return any of them.

"""
def findPeakElement(arr):
    n = len(arr)

    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i
    # Check for peak at the beginning
    if n > 1 and arr[0] > arr[1]:
        return 0
    # Check for peak at the end
    if n > 1 and arr[n - 1] > arr[n - 2]:
        return n - 1
    return -1  # No peak found (should not happen for valid input)


def findPeakbs(arr):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak element
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return mid
        # If the left neighbor is greater, move to the left half
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        # If the right neighbor is greater, move to the right half
        else:
            low = mid + 1

    return -1  # No peak found (should not happen for valid input)

# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    index = findPeakElement(arr)
    print("The index of a peak element is:", index) # Output: 7

    arr = [1, 2, 1, 3, 5, 6, 4]
    index = findPeakElement(arr)
    print("The index of a peak element is:", index) # Output: 1

    arr = [10, 20, 15, 2, 23, 90, 67]
    index = findPeakElement(arr)
    print("The index of a peak element is:", index) # Output: 1



    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    index = findPeakbs(arr)
    print("The index of a peak element is:", index) # Output: 7

    arr = [1, 2, 1, 3, 5, 6, 4]
    index = findPeakbs(arr)
    print("The index of a peak element is:", index) # Output: 1

    arr = [10, 20, 15, 2, 23, 90, 67]
    index = findPeakbs(arr)
    print("The index of a peak element is:", index) # Output: 1