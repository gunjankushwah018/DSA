# Approach: Binary Search
# Time Complexity: O(log N), where N is the input number 'n'
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def arrangeCoins(self, n):
        l = 1
        r = n
        ans = 0

        while l <= r:
            mid = (l + r)//2
            coins = mid*(mid+1)//2

            if coins <= n:
                ans = mid
                l = mid+1

            else:
                r = mid-1

        return ans
        