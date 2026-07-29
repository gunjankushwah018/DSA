# Approach:
# 1. Initialize variables to track the sign, the number being formed, and flags to indicate if the parsing has started or if a sign has been seen.
# 2. Iterate through each character in the input string:
#    - If the character is a space and parsing hasn't started, continue to the next character.
#    - If the character is a sign ('+' or '-'), set the sign accordingly and mark that a sign has been seen.
#    - If the character is a digit, update the number being formed and check for overflow/underflow conditions.
#    - If any other character is encountered, break the loop as it indicates the end of valid input.
# 3.check for overflow/underflow:
# - If the number being formed exceeds the 32-bit signed integer range, return the appropriate limit (-2^31 or 2^31 - 1).
# else, return the final number multiplied by the sign.

# Time complexity: O(n), where n is the length of the input string, as we are iterating through the string once.
# Space complexity: O(1), as we are using a fixed number of variables to store the

class Solution(object):
    def myAtoi(self, s):
        sign=1
        num=0
        started=False
        signSeen=False
        for ch in s:
            
            if ch ==" ":
                if started or signSeen:
                    break
                continue
            
            if ch in "+-":
                if started or signSeen:
                    break
                signSeen=True
                sign=-1 if ch =="-" else 1
                continue

            if ch.isdigit():
                started=True
                num=num*10+int(ch)

                if sign*num < -2**31 :
                    return -2**31
                if sign*num > 2**31-1:
                    return 2**31-1
            else:
                break

        return sign*num
