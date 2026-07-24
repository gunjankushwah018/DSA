# Approach:
#     1.create list to store the result
#     2. iterate through the string from the end to the start
#     3. skip the spaces
#     4. find the start and end of the word
#     5. append the word to the result list
#     6. join the result list with space and return the result
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.


class Solution(object):
    def reverseWords(self, s):
        result=[]
        i=len(s)-1

        while i>=0:

            while i >= 0 and s[i] == " ":
                i -= 1

            if i<0:
                break

            j = i

            while i>=0 and s[i]!=" ":
                i-=1

            result.append(s[i+1 : j+1])

        return " ".join(result)
        
        