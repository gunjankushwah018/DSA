# Approach: Expand Around Center
# 1. Iterate through the string and for each character, consider it as the center of a palindrome.
# 2. Expand around the center to find the longest palindrome for both odd and even length palindromes.
# Time Complexity: O(n^2), where n is the length of the string.
# Space Complexity: O(1), as we are using constant space.


class Solution(object):
    def longestPalindrome(self, s):
        if len(s)<=1:
            return s

        length=1
        start=0

        for i in range(len(s)):
            # odd length palindrome
            left=i
            right=i

            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                curr = right-left+1
                if curr>length:
                    length=curr
                    start=left
                
                left-=1
                right+=1

            # even length palindrome
            left=i
            right=i+1
            
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                curr = right-left+1
                if curr>length:
                    length=curr
                    start=left
                
                left-=1
                right+=1
                
        return s[start:start+length]
                    
