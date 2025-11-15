"""
Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

Input: Arr[] = {1,3,2}
Output: {2,1,3}
Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,1,3} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.

Input : Arr[] = {3,2,1}
Output: {1,2,3}
Explanation : As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the lowest permutation.

"""
# Solution class
class Solution:
    # Function to find next permutation
    def nextPermutation(self, nums):
        # Set index
        index = -1

        # Find decreasing point
        for i in range(len(nums) - 2, -1, -1):
            # If smaller found
            if nums[i] < nums[i + 1]:
                index = i
                break

        # If no such index
        if index == -1:
            # Reverse whole list
            nums.reverse()
            return

        # Find just greater element
        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index]:
                # Swap them
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Reverse part after index
        nums[index + 1:] = reversed(nums[index + 1:])

# Main driver
def main():
    # Input list
    nums = [1, 2, 3]

    # Create object
    sol = Solution()

    # Call function
    sol.nextPermutation(nums)

    # Print result
    print(" ".join(map(str, nums)))

# Run main
main()