# Approach: Stack
# Time complexity: O(n+m), where n is the length of nums1 and m is the length of nums2, as we are iterating through both arrays once.
# Space complexity: O(m), as we are using a stack to store elements from nums2, and a dictionary to store the next greater elements for each element in nums2.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        nge={}
        for x in nums2:
            while stack and x > stack[-1]:
                nge[stack[-1]]=x
                stack.pop()
            stack.append(x)

        while stack:
            ch=stack.pop()
            nge[ch] = -1

        ans=[]

        for x in nums1:
            ans.append(nge[x])
        
        return ans

