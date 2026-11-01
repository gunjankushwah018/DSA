# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input array nums.
# Space Complexity: O(n), as we are using an additional array ans of the same length as nums to store the averages.

class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        window_size = 2*k+1
        ans = [-1]*n

        if n < window_size:
            return ans

        window_sum = sum(nums[:window_size])

        for i in range(k, n-k):
            window_avg = window_sum // window_size
            ans[i] = window_avg

            if i < n-k-1:
                window_sum = window_sum - nums[i-k] + nums[i+k+1]

        return ans