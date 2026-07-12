# Optimal Solution:Greedy approach
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def canJump(self,nums):
        max_reach=0
        for i in range(len(nums)):
            if i>max_reach:
                return False
            max_reach=max(max_reach,i+nums[i])
        return True
