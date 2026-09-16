# Approach: HashMap
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        mp = {}
        count = 0
        
        # Store frequency of nums1 + nums2
        for a in nums1:
            for b in nums2:
                s = a+b
                mp[s] = mp.get(s,0)+1
        
        # Find required -(c + d)
        for c in nums3:
            for d in nums4:
                s = c+d
                count+=mp.get(-s,0)
        return count