# Approach: Binary Search
# Time Complexity: O(log n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def findPeakElement(self, nums):
        l = 0
        r = len(nums)-1

        while l<r :
            mid = (l+r)//2

            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid

        return l