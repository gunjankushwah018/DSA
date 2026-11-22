# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input array because we are iterating through the array once.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the current count of zeros and the best length of the subarray.

class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        max_len = 0
        zeros = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while zeros > 1:

                if nums[left] == 0:
                    zeros-=1

                left+=1
                
            # window [left, right] has at most one zero; one element is deleted
            max_len = max(max_len,right-left)

        return max_len