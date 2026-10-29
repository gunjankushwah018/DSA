# Approach: Sliding Window
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the variables, regardless of the input size.

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        window_sum = sum(arr[:k])
        count = 0

        if window_sum/k >= threshold:
            count+=1

        for i in range(k,len(arr)): 
            window_sum = window_sum-arr[i-k]+arr[i]
            
            if window_sum/k >= threshold:
                count +=1
        
        return count