# Approach:USe two queues to implement stack operations. The idea is to use one queue 
# for storing the elements and the other queue for reversing the order of elements during the push operation.
# Time Complexity O(n^2) for push operation, O(1) for pop, top and empty operations.
# Space Complexity O(n) for storing the elements in the queues.

class MyStack(object):

    def __init__(self):
        self.q1=[]
        self.q2=[]
        

    def push(self, x):
        self.q2.append(x)
        
        while self.q1:
            element=self.q1.pop(0)
            self.q2.append(element)
        self.q1,self.q2=self.q2,self.q1
        
    def pop(self):
        return self.q1.pop(0)
        

    def top(self):
        return self.q1[0]
        

    def empty(self):
        if self.q1:
            return False
        else:
            return True
        