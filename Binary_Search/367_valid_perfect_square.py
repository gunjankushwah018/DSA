# Approach: Binary Search
# Time Complexity: O(log N), where N is the input number
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def isPerfectSquare(self, num):
        l = 1
        r = num

        while l <= r :

            mid = (r + l)//2
            square = mid*mid
            if square == num:
                return True

            if square < num:
                l = mid+1

            else:
                r = mid - 1

        return False
