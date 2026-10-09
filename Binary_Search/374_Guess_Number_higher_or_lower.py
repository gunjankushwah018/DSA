# Approach: Binary Search
# Time Complexity: O(log N), where N is the range of numbers from 1 to n
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def guessNumber(self, n):
        l = 1
        r = n
        while l <= r:
            mid = (l+r)//2

            if guess(mid) == 0:
                return (mid)

            if guess(mid) == -1:
                r = mid - 1

            else:
                l = mid + 1