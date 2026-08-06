# Approach: Stack
# Time Complexity: O(n), where n is the length of the input string, as we are iterating through the string once.
# Space Complexity: O(n), as we are using a stack to store the characters, which in the worst case can take up to n space.

class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for ch in s:
            if stack:
                top=stack[-1]
                if ch==top:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return "".join(stack)