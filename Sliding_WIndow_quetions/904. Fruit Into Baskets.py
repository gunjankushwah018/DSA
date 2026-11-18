# Approach: Sliding Window
# Time Complexity: O(n), where n is the length of the input list because we are iterating through the list once.
# Space Complexity: O(1), as we are using a constant amount of extra space to store the counts of the fruits.

class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        count = {}
        max_len = 0
        for right in range(len(fruits)):

            count[fruits[right]] = count.get(fruits[right],0)+1

            while len(count) > 2:
                
                count[fruits[left]]-=1

                if count[fruits[left]] == 0:
                        del count[fruits[left]]

                left+=1
             
            max_len = max(max_len,right-left+1)   
        
        return max_len