# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the variables, regardless of the input size.

class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0
        window = s[:3]

        if len(set(window)) == 3:
            count += 1

        for i in range(3, len(s)):
            window = window[1:] + s[i]

            if len(set(window)) == 3:
                count += 1

        return count