# Approach : Hashset
# Time Complexity : O(n + m)
# Space Complexity : O(n + m)

class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        set1 = set(nums1)
        set2 = set(nums2)
        for ch in set1:
            if ch in set2:
                result.append(ch)
        return result        