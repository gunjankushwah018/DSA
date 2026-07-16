# Approach:
# 1. l=0
# 2. If s is empty, return True (an empty string is a subsequence of any string).
# 3. Iterate through the string t using a for loop.
# 4. If the current character in t matches the character at index l in s, increment l by 1.
# 5. If l reaches the length of s, return True (all characters in s have been found in t in order).
# 6. If the loop completes and l does not reach the length of s, return False (not all characters in s were found in t in order).

# Time Complexity: O(n), where n is the length of the string t. We may need to traverse the entire string t in the worst case.
# Space Complexity: O(1), as we are using a constant amount of space for the variable l.

class Solution(object):
    def isSubsequence(self, s, t):
        l=0
        if not s:
            return True
        for i in range(len(t)):
            if t[i]==s[l]:
                l+=1
                if l==len(s):
                    return True
        return False