# Approach: Binary Search
# Time Complexity: O(log N), where N is the length of the input array 'nums'
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def searchRange(self, nums, target):
        l = 0
        r = len(nums)-1
        first = -1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                first = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        
        l = 0
        r = len(nums)-1
        last = -1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid - 1
        
        return [first,last]