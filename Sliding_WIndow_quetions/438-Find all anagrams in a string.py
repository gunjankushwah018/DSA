# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input string because we are iterating through the string once.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the character counts.

class Solution(object):
    def findAnagrams(self, s, p):
        left=0
        right=len(p)-1
        result=[]
        p_count=[0]*26
        window_count=[0]*26

        if len(p)>len(s):
            return result

        for i in range(len(p)):
            p_count[ord(p[i])-ord("a")]+=1
        
        for i in range(len(p)):
            window_count[ord(s[i])-ord("a")]+=1

        while right<len(s):
            if window_count==p_count:
                result.append(left)
            if right+1<len(s):
                window_count[ord(s[left])-ord("a")]-=1
                window_count[ord(s[right+1])-ord("a")]+=1
            left+=1
            right+=1
            
        return result