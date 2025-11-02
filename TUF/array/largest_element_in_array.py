"""
 Given an array, we have to find the largest element in the array.
 
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example 2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 
 """


def largest_element(arr):
    n =len(arr)
    Largest = arr[0]

    for ele in arr:
        if ele > Largest:
            Largest = ele
    return Largest

print("The largest element in the array is:", largest_element([2, 5, 1, 3, 0]))