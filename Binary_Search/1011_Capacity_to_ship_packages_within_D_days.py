# Approach: Binary Search
# Time Complexity: O(n log m), where n is the number of weights and m is the sum of weights.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the pointers and variables, regardless of the input size.

class Solution(object):
    def shipWithinDays(self, weights, days):
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (l + r)//2

            total_days = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight <= mid:
                    current_weight += weight
                else:
                    total_days += 1
                    current_weight = weight

            if total_days <= days:
                r = mid - 1

            else:
                l = mid + 1
        return l