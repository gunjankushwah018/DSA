# Approach:Stack
# Time Complexity: O(n), where n is the number of asteroids in the input list.
# Space Complexity: O(n), where n is the number of asteroids in the input list, as we may need to store all asteroids in the stack.
    
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            destroyed = False

            if asteroid > 0:
                stack.append(asteroid)

            else:
                # collision condition
                while stack and stack[-1] > 0 and asteroid <0:

                    if stack[-1] < abs(asteroid):
                        stack.pop()

                    elif stack[-1] > abs(asteroid):
                        destroyed = True
                        break

                    else:
                        stack.pop()
                        destroyed = True
                        break

                if not destroyed:
                    stack.append(asteroid)

        return stack