"""
Docstring for TUF.binary_search.binary_search_on_answer.smallset_divisor

 You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'.
Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it,
the sum of the division's result is less than or equal to the given threshold value.

Example 1:
Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
Result: 3
Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

Example 2:
Input Format: N = 4, arr[] = {8,4,2,3}, limit = 10
Result: 2
Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9(4+2+1+2) <= 10 as the answer. So, 2 is the answer.
"""

def sum_of_divisions(arr, divisor):
    total = 0
    for num in arr:
        total += (num + divisor - 1) // divisor  # This is a way to calculate the ceiling of num/divisor
    return total

def smallest_divisor(arr, limit):
    left, right = 1, max(arr)
    result = right

    while left <= right:
        mid = left + (right - left) // 2
        if sum_of_divisions(arr, mid) <= limit:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result   


# Example usage:
if __name__ == "__main__":  
    arr = [1, 2, 3, 4, 5]
    limit = 8
    print(smallest_divisor(arr, limit))  # Output: 3

    arr = [8, 4, 2, 3]
    limit = 10
    print(smallest_divisor(arr, limit))  # Output: 2
    