# Approach: Stack + Adjacent cancellation
# Time complexity: O(n), where n is the length of the input string, as we are iterating through the string once.
# Space complexity: O(n), as we are using a stack to store the characters, which in the worst case can take up to n space.

class Solution(object):
    def makeGood(self, s):
        stack = []
        for ch in s:

            if stack and ch != stack[-1] and ch.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(ch)    
                
        return "".join(stack)