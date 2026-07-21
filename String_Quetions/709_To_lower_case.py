# Approach:
#     1. Iterate through each character in the string.
#     2. If the character is an uppercase letter, convert it to lowercase by adding 32 to its ASCII value.
#     3. Otherwise, keep the character as is.
#     4. Return the modified string.

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), as we are creating a new string to store the result.

class Solution(object):
    def toLowerCase(self, s):
        result=""
        for ch in s:
            if ch.isupper():
                c=ord(ch)+32
                result+=chr(c)
            else:
                result+=ch
        return result
        