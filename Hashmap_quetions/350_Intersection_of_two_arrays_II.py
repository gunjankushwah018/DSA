# Approach: Hashmap
# Time Complexity: O(n + m)
# Space Complexity: O(m)

class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        freq = {}
        for num in nums1:
            freq[num]=freq.get(num,0)+1
        
        for num in nums2:
            if freq.get(num,0)>0:
                result.append(num)
                freq[num]-=1
        return result       