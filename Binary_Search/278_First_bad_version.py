# Approach: Binary Search
# Time Complexity: O(log N), where N is the number of versions, as we are dividing the search space in half with each iteration.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def firstBadVersion(self, n):
        l = 0
        r = n

        while l <= r:
            mid = (l+r)//2

            if isBadVersion(mid):
                r = mid-1

            else:
                l = mid + 1

        return l