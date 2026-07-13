# LeetCode 73. Set Matrix Zeroes
# Trick used:
#     1. Set markers in the first row and first column.
#     2. Use a variable (col0) to track if the first column should be zeroed out.
#     3. Update the inner matrix based on the markers.
#     4. Fill the first row and first column based on the markers and col0 variable.
#      
#     Time Complexity: O(m*n) 
#     space Complexity: O(1) (in-place modification)


class Solution(object):
    def setZeroes(self, matrix):
        col0=1
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                col0=0
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        
        for j in range(1,len(matrix[0])):
            if matrix[0][0]==0:
                matrix[0][j]=0

        for i in range(len(matrix)):
            if col0==0:
                matrix[i][0]=0