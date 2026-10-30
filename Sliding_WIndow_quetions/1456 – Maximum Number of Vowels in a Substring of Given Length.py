# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the variables, regardless of the input size.

class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        length = 0

        for i in range(k):
            if s[i] in vowels:
                length += 1

        max_length = length
        
        for i in range(k,len(s)):
            
            if s[i-k] in vowels:
                length-=1

            if s[i] in vowels:
                length+=1
            
            max_length = max(max_length,length)
            
        return max_length