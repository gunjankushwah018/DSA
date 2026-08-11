# Approach: Monotonic Stack
# Time complexity: O(n), where n is the length of nums, as we are iterating through the array twice (once for the first pass and once for the second pass).
# Space complexity: O(n), as we are using a stack to store indices of elements in nums, and an array to store the next greater elements for each element in nums.

class Solution(object):
    def nextGreaterElements(self, nums):

        n=len(nums)
        stack=[]
        ans=[-1]*n

        for i in range(2*n):
            while stack:

                top=stack[-1]

                if nums[top] < nums[i % n]:
                    ans[top] = nums[i % n]
                    stack.pop()

                else:
                    break

            if i < n:
                stack.append(i % n)
                
        return ans
        

