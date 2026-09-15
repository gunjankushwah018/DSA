# Approach: HashMap + Array
# Time Complexity: O(1)
# Space Complexity: O(n)

import random
class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val):
        if val not in self.pos:
            self.pos[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False
                

    def remove(self, val):
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        self.arr[idx] = last
        self.pos[last] = idx

        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.arr)
        