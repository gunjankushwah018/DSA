# Approach:Stack
# Time Complexity: O(n), where n is the length of the input path.
# Space Complexity: O(n), where n is the length of the input path, as we may need to store all parts of the path in the stack.

class Solution(object):
    def simplifyPath(self, path):
        stack = []

        for part in path.split("/"):

            if part == "..":
                if stack:
                    stack.pop()

            elif part == "" or part == ".":
                pass

            else:
                stack.append(part)

        return "/"+"/".join(stack)
                
