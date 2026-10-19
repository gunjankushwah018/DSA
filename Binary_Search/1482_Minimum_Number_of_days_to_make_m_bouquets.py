# Approach: Binary Search
# Time Complexity: O(n log m), where n is the number of flowers and m is the range of days (max bloom day - min bloom day).
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def minDays(self, bloomDay, m, k):

        if m * k > len(bloomDay):
            return -1

        l = min(bloomDay)
        r = max(bloomDay)

        while l <= r :
            mid = (l + r)//2

            total_bouquets = 0
            flowers = 0
            for day in bloomDay:
                if day <= mid:
                    flowers += 1

                    if flowers == k:
                        total_bouquets += 1
                        flowers = 0
                else:
                    flowers = 0 

            if total_bouquets >= m:
                r = mid - 1

            else:
                l = mid + 1
                
        return l