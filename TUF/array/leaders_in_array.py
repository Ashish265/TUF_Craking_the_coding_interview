"""
Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.

Example 1:
Input:
 arr = [4, 7, 1, 0]
Output:
 7 1 0
Explanation:
 Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

Example 2:
Input:
 arr = [10, 22, 12, 3, 0, 6]
Output:
 22 12 6
Explanation:
 6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.

"""



def find_leaders(arr):
    leaders = []
    max_right = arr[-1]
    n = len(arr)
    leaders.append(max_right)

    # Traverse the array from right to left
    for  i in range(n-1,-1,-1):
        if arr[i] > max_right:
            max_right = arr[i]
            leaders.append(max_right)


    return leaders[::-1]  # Reverse to maintain the order


# Example usage
arr = [10, 22, 12, 3, 0, 6]
print(find_leaders(arr))  # Output: [22, 12, 6]
