# Approach:Two pointers approach is used to compress the string in place. 
# The read pointer iterates through the input list of characters,
# while the write pointer keeps track of the position to write the compressed characters.
# The algorithm counts consecutive characters and writes the character followed by its count (if greater than 1) to the write position.
# Time complexity: O(n), where n is the length of the input list, as we are iterating through the list once.
# Space complexity: O(1), as we are using a fixed number of variables to store the read and write pointers, the current character,
# and the count of consecutive characters.

class Solution(object):
    def compress(self, chars):
        read=0
        write=0
        n=len(chars)
        while read < n:
            current=chars[read]
            count=0

            while read < n and chars[read]==current:
                count+=1
                read+=1
            chars[write]=current
            write+=1
             
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write    

