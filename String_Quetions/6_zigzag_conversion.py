# Approach: The idea is to simulate the zigzag pattern by keeping track of the current row and the direction of movement (down or up).
# Time complexity: O(n), where n is the length of the input string, as we are iterating through the string once.
# Space complexity: O(n), as we are using a list to store the characters for each row, which in the worst case can take up to n space.

class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1 or numRows >= len(s):
            return s

        current_row=0
        direction=1
        rows=[""]*numRows

        for ch in s:
            rows[current_row]+=ch

            if current_row == 0:
                direction=1
            elif current_row == numRows -1:
                direction=-1

            current_row += direction
    
        return "".join(rows)