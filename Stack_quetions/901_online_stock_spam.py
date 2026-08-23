# Approach: Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        spam = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price,prev_spam = self.stack.pop()
            spam += prev_spam
        self.stack.append((price,spam))
        return spam
        