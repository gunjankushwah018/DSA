# Approach:
# 1. Initialize two pointers, l and r, to the start and end of the string respectively
# 2. While l is less than r, swap the characters at positions l and r
# 3. Increment l and decrement r
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(1) since we are modifying the string in place


class Solution(object):
    def reverseString(self, s):
        l=0
        r=len(s)-1

        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1