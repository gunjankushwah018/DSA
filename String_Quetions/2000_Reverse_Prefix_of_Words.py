# Approach: Two Pointers
# Time complexity: O(n)
# Space complexity: O(n) since we are converting the string to a list for in-place modifications

class Solution(object):
    def reversePrefix(self, word, ch):
        word=list(word)
        for i in range(len(word)):
            if ch==word[i]:
                l=0
                r=i
                while l<r:
                    word[l],word[r]=word[r],word[l]
                    l+=1
                    r-=1
                return "".join(word)
        return "".join(word)    