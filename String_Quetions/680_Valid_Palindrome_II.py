# approach: Two Pointers
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def validPalindrome(self, s):
        def check(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return check(l+1,r) or check(l,r-1)         
        return True
        