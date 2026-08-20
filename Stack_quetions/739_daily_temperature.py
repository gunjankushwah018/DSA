# Approach: Monotonic Stack
#     Use a stack to keep track of the indices of the temperatures.
#     Iterate through the list of temperatures:
#         - While the stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack,
#         pop the index from the stack and calculate the number of days until a warmer temperature for that index.
#         - Push the current index onto the stack.
# Time Complexity: O(n), where n is the number of temperatures in the input list.
# Space Complexity: O(n), where n is the number of temperatures in the input list, as we may need to store all indices in the stack.

class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans=[0]*len(temperatures)
        stack=[0]

        for i in range(1,len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans