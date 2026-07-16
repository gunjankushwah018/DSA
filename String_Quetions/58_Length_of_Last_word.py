# Approach:
# 1. Initialize a variable `count` to 0 to keep track of the length of the last word.
# 2. Iterate through the string `s` in reverse order (from the last character to the first).
# 3. If the current character is a space and `count` is 0, continue to the next character (skip leading spaces).
# 4. If the current character is an alphabetic character, increment `count`.
# 5. If the current character is a space and `count` is not 0, return `count`.

# Time Complexity: O(n), where n is the length of the string `s`. We may need to traverse the entire string in the worst case.
# Space Complexity: O(1), as we are using a constant amount of space for the `count` variable.

class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ' and count==0:
                continue
            elif s[i].isalpha():
                count+=1
            else:
                return count
        return count
        