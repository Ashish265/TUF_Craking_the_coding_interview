"""
Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

Examples:

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5

"""


class Solution:
    def selectionSort(self, nums):

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums
    

selection_sort = Solution()
print(selection_sort.selectionSort([7, 4, 1, 5, 3]))