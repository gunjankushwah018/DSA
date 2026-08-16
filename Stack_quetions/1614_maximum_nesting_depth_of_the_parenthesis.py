# Approach :
# 1. Initialize two variables `depth` and `max_depth` to 0. `depth` will keep track of the current depth of nested parentheses, while `max_depth` will store the maximum depth encountered.
# 2. Iterate through each character in the input string `s`.
# 3. For each character:
#     - If the character is `"("`, increment `depth` by 1 and update `max_depth` to be the maximum of `max_depth` and `depth`.
#     - If the character is `")"`, decrement `depth` by 1.
# Time complexity: O(n), where n is the length of the input string `s`.
# Space complexity: O(1), as we are using a constant amount of space for the `depth` and `max_depth` variables.

class Solution(object):
    def maxDepth(self, s):
        depth = 0
        max_depth = 0
        for ch in s:
            if ch == "(":
                depth+=1
                max_depth = max(max_depth,depth)
            elif ch == ")":
                depth -=1
        return max_depth