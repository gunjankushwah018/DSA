# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input string because we are iterating through the string once.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the character counts.

class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        max_len = 0
        max_freq = 0
        count = {}

        for right in range(len(s)):

            count[s[right]] = count.get(s[right],0)+1

            max_freq = max(max_freq,count[s[right]])

            window_len = right-left+1

            if window_len - max_freq > k:

                count[s[left]] -= 1

                left += 1

            max_len = max(max_len, right-left+1)

        return max_len