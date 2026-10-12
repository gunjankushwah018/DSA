# Approach: Binary Search
# Time Complexity: O(log N), where N is the length of the input list 'letters'
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters)-1
        while left <= right:
            mid = (left + right)//2

            if letters[mid] <= target:
                left = mid + 1

            else:
                right = mid - 1

        return letters[left % len(letters)]
