# Approach: Stack
# Time Complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        result = 0
        sign = +1

        for ch in s:
            
            if ch.isdigit():
                num = num*10 + int(ch)

            elif ch in "+-":
                result += sign * num
                num = 0
                sign = 1 if ch == "+" else -1

            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = +1
                num = 0

            elif ch == ")":
                result += sign * num
                num =0 
                result = stack.pop()*result+stack.pop()
        return result + sign*num