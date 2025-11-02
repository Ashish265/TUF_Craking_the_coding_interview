"""
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. 
It does not matter what you leave beyond the first k elements.

Input: arr[]=[1,1,2,2,2,3,3]
Output: [1,2,3,_,_,_,_]
Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

Input: arr[]=[1,1,1,2,2,3,3,3,3,4,4]
Output: [1,2,3,4,_,_,_,_,_,_,_]
Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.

"""

def remove_duplicates(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    unique_index = 1

    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[unique_index] = arr[i]
            unique_index += 1

    for i in range(unique_index, n):
        arr[i] = "_"
    
    return arr

print("Array after removing duplicates:", remove_duplicates([1, 1, 2, 2, 2, 3, 3]))
print("Array after removing duplicates:", remove_duplicates([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]))