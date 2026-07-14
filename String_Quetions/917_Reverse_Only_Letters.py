# Approach: Two Pointers
# 1. Initialize two pointers, l and r, to the start and end of the string respectively
# 2. Convert the string to a list to allow in-place modifications
# 3. While l < r, check if the characters at l and r are letters. If
#     - If s[l] is not a letter, increment l
#     - If s[r] is not a letter, decrement r
#     - If both are letters, swap them and move both pointers inward

#  Time Complexity: O(n) where n is the length of the string
#  Space Complexity: O(n) since we are converting the string to a list for in-place modifications

class Solution(object):
    def reverseOnlyLetters(self, s):
        
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            if not s[l].isalpha():
                l+=1
            elif not s[r].isalpha():
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return "".join(s)