# Approach: Hashmap
# Time Complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                current_index = i
                previous_index = hash[nums[i]]
                if current_index - previous_index <= k:
                    return True
                else:
                    hash[nums[i]] = current_index
            else:
                hash[nums[i]] = i
        return False