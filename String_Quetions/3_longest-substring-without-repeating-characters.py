# Approach: Sliding Window
#     1. Initialize two pointers, left and right, both set to 0.
#     2. Create a set to store the characters in the current window.
#     3. Iterate through the string using the right pointer.
#     4. If the character at the right pointer is not in the set, add it to the set and update the maximum length.
#     5. If the character at the right pointer is already in the set, remove the character at the left pointer from the set and move the left pointer to the right.
#     6.and Repeat steps 4 and 5 until the right pointer reaches the end of the string.
#     7.and Return the maximum length of the substring without repeating characters.
    
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set 


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        right=0
        store=set()
        max_len=0
        while right<len(s):
            if s[right] in store :
                store.remove(s[left])
                left+=1
            else:
                store.add(s[right])
                max_len=max(len(store),max_len)
                right+=1
        return max_len