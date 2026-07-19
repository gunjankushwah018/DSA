# Approach: Optimized Approach
# Time complexity: O(n), where n is the length of the string s.
# Space complexity: O(1), as we are using a fixed-size array of length 26
    
class Solution(object):
    def firstUniqChar(self, s):
        count=[0]*26
        for i in range(len(s)):
            index=ord(s[i])-ord("a")
            count[index]+=1
        for i in range(len(s)):
            if count[ord(s[i])-ord("a")]==1:
                return i
        return-1    

        