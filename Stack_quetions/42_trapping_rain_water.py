# Approach: Two pointer approach
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height)-1

        rightmax=0
        leftmax=0
        water=0

        for i in range(len(height)):

            while left < right :

                if height[left] < height[right]:

                    if height[left] >= leftmax:
                        leftmax = height[left]

                    else:
                        water += leftmax - height[left]
                    left +=1

                else:
                     
                    if height[right] >= rightmax:
                        rightmax = height[right]
                    
                    else:
                        water += rightmax - height[right]
                    right -= 1
        return water
