# Approach: The idea is to use a stack to keep track of the opening brackets.
# When we encounter an opening bracket,
# we push it onto the stack. When we encounter a closing bracket,
# we check if the stack is empty or if the top of the stack does not match the corresponding opening bracket.
# If either condition is true, the string is not valid. At the end, if the stack is empty, the string is valid.
# Time complexity: O(n), where n is the length of the input string, as we are iterating through the string once.
# Space complexity: O(n), as we are using a stack to store the opening brackets, which in the worst case can take up to n space.


class Solution(object):
    def isValid(self, s):

        stack=[]

        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            else:
                if not stack:
                    return False

                top=stack.pop()

                if top!=pairs[ch]:
                    return False
        return len(stack)==0
            
        