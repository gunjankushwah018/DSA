# Approach: Stack
# Time complexity: O(n), where n is the length of the input list, as we are iterating through the list once.
# Space complexity: O(n), as we are using a stack to store the scores, which in the worst case can take up to n space.

class Solution(object):
    def calPoints(self, operations):
        stack = []
        for ch in operations:

            if ch not in ['C','D','+']:
                stack.append(int(ch))

            elif ch == 'C':
                stack.pop()

            elif ch == 'D':
                top = stack[-1]
                stack.append(2*top)

            elif ch == '+':
                element = stack[-1]+stack[-2]
                stack.append(element) 

        return sum(stack)    