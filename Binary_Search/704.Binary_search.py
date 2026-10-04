# Approach: Binary Search
# Time Complexity: O(log N), where N is the number of elements in the input list, as we are dividing the search space in half with each iteration.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid+1
            
            elif nums[mid] > target:
                right = mid-1

        return -1