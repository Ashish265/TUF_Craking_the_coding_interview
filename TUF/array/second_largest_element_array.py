"""
Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.

"""


def second_smallest_largest(arr):
    n = len(arr)
    if n < 2:
        return -1, -1
    
    first_smallest = float('inf')
    second_smallest = float('inf')
    first_largest = float("-inf")
    second_largest = float("-inf")

    for ele in arr:
        if ele < first_smallest:
            second_smallest = first_smallest
            first_smallest = ele
        elif first_smallest < ele < second_smallest:
            second_smallest = ele

        if ele > first_largest:
            second_largest = first_largest
            first_largest = ele
        elif first_largest > ele > second_largest:
            second_largest = ele

    return second_largest, second_smallest


print("Second Largest and Second Smallest elements are:", second_smallest_largest([1, 2, 4, 7, 7, 5]))