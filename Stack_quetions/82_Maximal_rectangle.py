# Approach: Stack
# Time Complexity: O(m*n)
# Space complexity: O(n)

class Solution(object):
    def maximalRectangle(self, matrix):

        #Largest rectangle in histogram
        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            
            for i in range(len(heights)+1):
                curr = 0 if i == len(heights) else heights[i]

                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]

                    width = i if not stack else i - stack[-1]-1

                    max_area = max(max_area,h * width)

                stack.append(i)

            return max_area

        m = len(matrix)
        n = len(matrix[0])
        heights = [0] * n
        ans = 0

        for i in range(m):

            # heights update karo
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # LC 84
            area = largestRectangleArea(heights)

            ans = max(ans, area)

        return ans