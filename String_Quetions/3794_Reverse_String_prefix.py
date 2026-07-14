# Approach: Two Pointers
# 1. Initialize two pointers, l and r, to the start and end of the prefix respectively
# 2. Convert the string to a list to allow in-place modifications
# 3. While l < r, swap the characters at l and r and move both pointers inward
# 4.and return the modified string
# Time Complexity: O(n) 
# Space Complexity: O(n) since we are converting the string to a list for in-place modifications


class Solution(object):
    def reversePrefix(self, s, k):
        l=0
        r=k-1
        s=list(s)
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return "".join(s)

