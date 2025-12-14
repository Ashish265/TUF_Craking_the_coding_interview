"""
Docstring for TUF.binary_search.search_element_rotated_array

Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k.
The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

Input:nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output :4
Explanation : Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3
Output :-1
Explanation :Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.

"""

class Solution:
    # Function to search target in rotated sorted array using binary search
    def search(self, nums, target):
        # Set initial search space
        low = 0
        high = len(nums) - 1

        # Run loop while valid search space exists
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2

            # If target found at mid, return index
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[low] <= nums[mid]:
                # If target lies in left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # Target not found
        return -1

# Driver code
nums = [4,5,6,7,0,1,2]
target = 0

obj = Solution()
result = obj.search(nums, target)

print(result)