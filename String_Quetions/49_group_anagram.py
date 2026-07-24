# Approach:
# 1. Create a dictionary to store the grouped anagrams.
# 2. Iterate through each word in the input list.
# 3. For each word, create a count of characters (using a list of size 26 for lowercase letters).
# 4.and Use the character count as a key in the dictionary. If the key already exists, append the word to the corresponding list; otherwise, create a new list with the word.
# 5. Return the values of the dictionary as a list of grouped anagrams.
# Time Complexity: O(n * k), where n is the number of words in the input list and k is the maximum length of a word.
# Space Complexity: O(n * k), where n is the number of words in the input list and k is the maximum length of a word.

class Solution(object):
    def groupAnagrams(self, strs):
        dic={}
        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            key=tuple(count)
            if key in dic:
                dic[key].append(word)
            else:
                dic[key]=[word]
        return list(dic.values())
