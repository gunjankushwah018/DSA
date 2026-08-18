# Approach:
#     Use a stack to evaluate the Reverse Polish Notation (RPN) expression.
#     Iterate through each token in the input list:
#         - If the token is an operator (+, -, *, /), pop the top two elements from the stack, apply the operator, and push the result back onto the stack.
#         - If the token is a number, convert it to an integer and push it onto the stack.
#         return the top element of the stack as the final result after processing all tokens.
# Time Complexity: O(n), where n is the number of tokens in the input list.
# Space complexity: O(n), where n is the number of tokens in the input list, as we may need to store all numbers in the stack.

class Solution(object):
    def evalRPN(self, tokens):
        ans = []
        for ch in tokens:
            if ch in "+-*/":
                b = ans.pop()
                a = ans.pop()
                if ch == "*":
                    ans.append(a * b)
                elif ch == "/":
                    # int(float(a) / b) truncates toward zero correctly
                    ans.append(int(float(a) / b))
                elif ch == "+":
                    ans.append(a + b)
                elif ch == "-":
                    ans.append(a - b)
            else:
                ans.append(int(ch))
                
        return ans[0]