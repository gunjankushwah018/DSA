# Approach:
#     Use two stacks: one for the actual elements and another to keep track of the minimum element at each level.
#     and implement the following methods:
#         - push(value): Pushes an element onto the stack.
#         - pop(): Removes the element on top of the stack.
#         - top(): Gets the top element of the stack.
#         - getMin(): Retrieves the minimum element in the stack.
# Time Complexity: O(1) for all operations.
# Space Complexity: O(n), where n is the number of elements in the stack.

class MinStack(object):

    def __init__(self):
        self.min_q = []
        self.q = []

    def push(self, value):
        self.q.append(value)
        
        if not self.min_q:
            self.min_q.append(value)
        else:
            self.min_q.append(min(value,self.min_q[-1]))
        
    def pop(self):
        self.q.pop()
        self.min_q.pop()
    
    def top(self):
        return self.q[-1]

    def getMin(self):
        return self.min_q[-1]
