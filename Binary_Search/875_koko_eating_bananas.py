# Approach: Binary Search
# Time Complexity: O(n log m), where n is the number of piles and m is the maximum number of bananas in a pile.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l+r)//2
            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1)//mid
            
            if total_hours <= h:
                r = mid - 1

            else:
                l = mid + 1

        return l
        