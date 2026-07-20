# Approach: Two Pointers
# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result=[]
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        while i<len(word1):
            result.append(word1[i])
            i+=1
        while j<len(word2):
            result.append(word2[j])
            j+=1
        return "".join(result)           

