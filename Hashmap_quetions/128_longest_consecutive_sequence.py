# Approach: HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def longestConsecutive(self, nums):

        nums_set = set(nums)
        ans = 0

        for ch in nums_set:

            # Sequence ka starting point
            if ch - 1 not in nums_set:

                l = 1
                i = 1

                while ch + i in nums_set:
                    i += 1
                    l += 1

                ans = max(ans, l)

        return ans