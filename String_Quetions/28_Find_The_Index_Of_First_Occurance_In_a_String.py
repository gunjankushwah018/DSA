# Approach:Broute Force
# 1. Iterate through the haystack string from index 0 to len(haystack)-len(needle)+1.
# 2. For each index i, initialize a variable j to 0.
# 3. While j is less than the length of needle and the character at haystack[i+j] matches the character at needle[j], increment j by 1.
# 4. If j reaches the length of needle, return the current index i (the starting index of the first occurrence of needle in haystack).
# 5.and If the loop completes and j does not reach the length of needle, return -1 (needle is not found in haystack).
# Time Complexity: O((n-m+1)*m), where n =len(haystack) and m=len(needle).
# Space Complexity: O(1), as we are using a constant amount of space for the variables i and j.

class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(0,len(haystack)-len(needle)+1):
            j=0
            while j<len(needle) and haystack[i+j]==needle[j]:
                j+=1
                if j==len(needle):
                    return i
        return -1