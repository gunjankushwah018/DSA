# Approach: Binary Search
# Time Complexity: O(n log m), where n is the number of elements in the array and m is the range of possible sums (max sum - min sum).
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def splitArray(self, nums, k):
        l = max(nums)
        r = sum(nums)

        while l <= r:
            mid = (l + r)//2

            total = 0
            subarrays = 1

            for num in nums:
                if total + num > mid:
                    subarrays += 1
                    total = num
                else:
                    total += num

            if subarrays > k:
                l = mid+1
            else:
                ans = mid
                r = mid-1
                
        return ans
