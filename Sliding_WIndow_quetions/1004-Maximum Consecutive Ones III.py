# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input list because we are iterating through the list once.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the counts of the fruits.

class Solution(object):
    def longestOnes(self, nums, k):
            left = 0
            max_len = 0
            zeros_count = 0
            count = {}

            for right in range(len(nums)):

                count[nums[right]] = count.get(nums[right],0)+1

                if nums[right] == 0:
                    zeros_count+=1

                window_len = right-left+1

                while zeros_count > k:

                    if nums[left] == 0:
                        zeros_count-=1
                        
                    left += 1

                max_len = max(max_len, right-left+1)
            return max_len