# Approach: Sliding Window
# Time Complexity: O(nlogn), where n is the length of the input list because we need to sort the list first.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the minimum difference.

class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        min_diff = float('inf')

        for i in range(len(nums)-k+1):

            diff = nums[i+k-1] - nums[i]
            min_diff = min(diff,min_diff)
        
        return min_diff