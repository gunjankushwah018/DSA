# Approach: Count the frequency of each character in both strings and compare the counts.

# Time Complexity: O(n), where n is the length of the strings (since we are iterating through both strings once).
# Space Complexity: O(1), as we are using a fixed-size array of length 26

class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        else:
            count=[0]*26
            for i in range(len(s)):
                count[ord(s[i])-ord("a")]+=1
                count[ord(t[i])-ord("a")]-=1
            for ch in count:
                if ch!=0:
                    return False
            return True
        
            