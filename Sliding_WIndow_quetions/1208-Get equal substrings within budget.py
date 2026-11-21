# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input strings because we are iterating through the strings once.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the current cost and the best length of the substring.

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        
        left = 0
        current_cost = 0
        best = 0

        for right in range(len(s)):

            current_cost += abs(ord(s[right])-ord(t[right]))

            while current_cost > maxCost:
                current_cost -= abs(ord(s[left])-ord(t[left]))
                left += 1

            best = max(best,right-left+1)

        return best