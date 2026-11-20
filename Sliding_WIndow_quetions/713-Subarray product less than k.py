# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input list because we are iterating through the list once.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the counts of the fruits.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        left = 0
        count = 0
        window_product = 1

        for right in range(len(nums)):

            window_product *= nums[right]
           
            while window_product >= k:
                    window_product //= nums[left]
                    left += 1

            count += right-left+1

        return count