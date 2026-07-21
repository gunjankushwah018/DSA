# Approach:
# 1. Check if the word is all uppercase using the isupper() method.
# 2. Check if the word is all lowercase using the islower() method.
# 3. Check if the first letter is uppercase and the rest of the letters are lowercase using isupper() and islower() methods.
# When any of the above conditions are satisfied, return True. Otherwise, return False.

# time Complexity: O(n), where n is the length of the word.
# Space Complexity: O(1), as we are using a constant amount of space.

class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper():
            return True

        elif word.islower():
            return True

        elif word[0].isupper() and word[1:].islower():
            return True
        
        else:
            return False