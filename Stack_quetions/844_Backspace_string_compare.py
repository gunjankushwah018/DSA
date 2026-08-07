# Approach :
#     Two pointers approach is used to compare the two strings from the end, skipping the characters that are backspaced.
# Time complexity: O(n + m), where n and m are the lengths of the input strings s and t, as we are iterating through both strings once.
# Space complexity: O(1), as we are using a constant amount of space for the pointers

class Solution(object):
    def backspaceCompare(self, s, t):
        skipS=0
        skipT=0

        i=len(s)-1
        j=len(t)-1

        while i>=0 or j>=0:

            #find the next valid character in s
            while i>=0:
                if s[i]=='#':
                    skipS+=1
                    i-=1
                elif skipS>0:
                    skipS-=1
                    i-=1
                else:
                    break

            #find the next valid character in t
            while j>=0:
                if t[j]=='#':
                    skipT+=1
                    j-=1
                elif skipT>0:
                    skipT-=1
                    j-=1
                else:
                    break

            # compare valid characters
            if i>=0 and j>=0:
                if s[i]!=t[j]:
                    return False
            elif i>=0 or j>=0:
                return False

            i-=1
            j-=1

        return True        
