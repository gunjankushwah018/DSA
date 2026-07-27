# Approach: Sliding Window
# 1.create a frequency count of the characters in string p.
# 2. create a frequency count of the characters in the first window of string s with the same length as p.
# 3. slide the window one character at a time, updating the frequency count of the characters in the window and checking if it matches the frequency count of p.
# 4. If the frequency counts match, add the starting index of the window to the result list.
# 5. Return the result list containing all starting indices of anagrams of p in s.

# Time complexity: O(n), where n is the length of string s, as we are iterating through the string once.
# Space complexity: O(1), as we are using a fixed-size array of length 26


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
        
            