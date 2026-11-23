# Approach : Recursion
# Time Complexity : O(n) - The time complexity of the recursive approach is O(n) because we are making two recursive calls for each value of n, leading to an exponential number of calls. However, due to overlapping subproblems, the actual time complexity can be reduced to O(n) with memoization.
# Space Complexity : O(n) - The space complexity is O(n) due to the recursion stack.

def fib(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr