# Approach used:- two pointer approach
# Time complexity: O(n+m) where n is the length of nums1 and m is the length of nums2
# Space complexity: O(1) as we are not using any extra space

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l=m-1
        r=n-1
        k=m+n-1
        while r>=0:
            if l>=0 and nums1[l]>nums2[r]:
                nums1[k]=nums1[l]
                l-=1
                

            else:
                nums1[k]=nums2[r]
                r-=1
                
            k-=1
        return nums1
