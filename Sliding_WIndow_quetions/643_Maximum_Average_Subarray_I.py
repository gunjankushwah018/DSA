# Approach: Sliding Window
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the variables, regardless of the input size.

class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum = window_sum-nums[i-k]+nums[i]
            max_sum = max(max_sum,window_sum)
        
        return max_sum / float(k)
