# Approach: Stack
# Time COmplexity: O(n), where n is the length of the input string, as we are iterating through the string once.
# Space Complexity: O(n), as we are using a stack to store the characters, which in the worst case can take up to n space.

class Solution(object):
    def removeOuterParentheses(self, s):
            stack = []
            depth = 0
            for ch in s:
                if ch == '(':
                    if depth:
                        stack.append(ch)
                    depth+=1

                elif ch == ')':
                    depth-=1
                    if depth:
                        stack.append(ch)
            return "".join(stack)
        