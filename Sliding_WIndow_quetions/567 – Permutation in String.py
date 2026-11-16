# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input string because we are iterating through the string once.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the character counts.

class Solution(object):
    def checkInclusion(self, s1, s2):
        left=0
        right=len(s1)-1
        s1_count=[0]*26
        window_count=[0]*26

        if len(s1)>len(s2):
            return False

        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord("a")]+=1
        
        for i in range(len(s1)):
            window_count[ord(s2[i])-ord("a")]+=1

        while right<len(s2):
            if window_count==s1_count:
                return True
            if right+1<len(s2):
                window_count[ord(s2[left])-ord("a")]-=1
                window_count[ord(s2[right+1])-ord("a")]+=1
            left+=1
            right+=1
            
        return False
        