# Approach: Recursion
# Time Complexity: O(log n) - The time complexity of the recursive approach is O(log n) because we are dividing the number by 2 in each recursive call, leading to a logarithmic number of calls.
# Space Complexity: O(log n) - The space complexity is O(log n) due to the recursion stack.

class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True

        if n<=0 or n%2 != 0:
            return False

        return self.isPowerOfTwo(n//2)