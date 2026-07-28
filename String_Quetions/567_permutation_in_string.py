# Approach: Sliding Window
# 1. Create a frequency count of the characters in string s1.
# 2. Create a frequency count of the characters in the first window of string s2 with the same length as s1.
# 3. Slide the window one character at a time, updating the frequency count of the characters in the window and checking if it matches the frequency count of s1.
# 4. If the frequency counts match, return True, indicating that a permutation of s1 exists in s2.

# Time complexity: O(n+m), where n is the length of string s1 and m is the length of string s2, as we are iterating through both strings once.
# Space complexity: O(1), as we are using a fixed-size array of length 26

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
        
            