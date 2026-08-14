# Approach:
# 1. Initialize a variable `depth` to 0, which will keep track of the current depth in the folder structure.
# 2. Iterate through each command in the `logs` list.
# 3. For each command:
#     - If the command is `"../"`, check if `depth` is greater than 0. If it is, decrement `depth` by 1 (move up one level).
#     - If the command is `"./"`, do nothing (stay in the current folder).
#     - If the command is any other string (indicating moving into a subfolder), increment `depth` by 1 (move down one level).
# time complexity: O(n), where n is the number of commands in the `logs` list.
# Space complexity: O(1), as we are using a constant amount of space for the `depth` variable.

class Solution(object):
    def minOperations(self, logs):
        depth = 0
        for ch in logs:

            if ch == "../":
                if depth > 0:
                    depth -=1
                
            elif ch == "./":
                pass

            else:
                depth +=1

        return depth