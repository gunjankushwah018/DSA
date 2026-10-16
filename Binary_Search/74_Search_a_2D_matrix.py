# Approach: Binary Search
# Time Complexity: O(log (m*n)), where m is the number of rows and n is the number of columns in the input matrix.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = (m*n) - 1

        while l <= r:
            mid = (l + r)// 2

            row = mid//n
            col = mid % n

            if matrix[row][col] == target:
                return True

            if matrix[row][col] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False