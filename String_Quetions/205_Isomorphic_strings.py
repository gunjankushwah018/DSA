# Approach: Optimized Approach
# 1. create two dictionaries, s_disc and t_disc, to store the mapping of characters from string s to string t and vice versa.
# 2. Iterate through the characters of both strings simultaneously.
# 3. For each character pair (s_char, t_char), check if s_char is already in s_disc:
#    - If it is, check if the mapped character in s_disc matches t_char. If not, return False.
#    - If it is not, check if t_char is already in t_disc. If it is, return False (since t_char is already mapped to a different character).
#    - If both checks pass, add the mapping of s_char to t_char in s_disc and t_char to s_char in t_disc.

# Time Complexity: O(n), where n is the length of the strings s and t.
# Space Complexity: O(n), as we are using two dictionaries to store the mappings of characters.



class Solution(object):
    def isIsomorphic(self, s, t):
        
        if len(s)!=len(t):
            return False
        
        s_disc={}
        t_disc={}
        
        for i in range(len(s)):
            s_char=s[i]
            t_char=t[i]
                
            if s_char in s_disc:
                if s_disc[s_char]!=t_char:
                    return False
            else:
                if t_char in t_disc:
                    return False
                    
                s_disc[s_char]=t_char
                t_disc[t_char]=s_char
        return True        