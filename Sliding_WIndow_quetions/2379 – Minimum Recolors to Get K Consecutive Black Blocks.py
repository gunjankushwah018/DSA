# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input string blocks.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the count of white blocks and the minimum recolor count.

class Solution(object):
    def minimumRecolors(self, blocks, k):
        window = blocks[:k]
        count = 0

        for ch in window:
            if ch == "W":
                count += 1

        min_recolor = count

        for i in range(k,len(blocks)):

            if blocks[i-k] == "W":
                count -= 1
            
            if blocks[i] == "W":
                count += 1

            min_recolor = min(min_recolor,count)

        return min_recolor