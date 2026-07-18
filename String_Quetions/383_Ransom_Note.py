# Approacgh: Count the frequency of each character in the magazine and then check if the ransom note can be constructed from it.
# 1.and If the length of ransomNote is greater than magazine, return False (since we cannot construct a longer string from a shorter one).
# 2.and If the length of ransomNote is less than or equal to magazine, initialize a count array of size 26 (for each letter in the alphabet) to keep track of the frequency of each character in the magazine.
# 3.and Iterate through the magazine string and increment the count for each character.
# 4.and Iterate through the ransomNote string and decrement the count for each character.
# 5.and If any count becomes negative, return False (since we cannot construct the ransom note from the magazine).
# Time Complexity: O(n+m), where n is the length of ransomNote and m is the length of magazine.
# Space Complexity: O(1), as we are using a fixed-size array of length 26.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count=[0]*26
        for i in range(len(magazine)):
            count[ord(magazine[i])-ord("a")]+=1
        for i in range(len(ransomNote)):
            count[ord(ransomNote[i])-ord("a")]-=1
        for ch in count:
            if ch<0:
                return False
        return True