# Approach:
# 1. Initialize two pointers, l and r, to the start and end of the string respectively
# 2. Convert the string to a list to allow in-place modifications
# 3. for every 2k characters in the string, reverse the first k characters
# 4.and return the modified string

# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n) since we are converting the string to a list for in-place modifications



class Solution(object):
    def reverseStr(self, s, k):
        s=list(s)
        for i in range(0,len(s),2*k):
            left=i
            right=min(i+k-1,len(s)-1)
            while left<right:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)