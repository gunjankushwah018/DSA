class Solution(object):
    def thirdMax(self, nums):
        f = s = t =None

        for num in nums:

            if num==f or num==s or num==t:
                continue

            if f==None or num>f:
                t=s
                s=f
                f=num
            
            elif s==None or num>s:
                t=s
                s=num

            elif t==None or num>t:
                t=num

        if t==None:
            return f

        return t

#  time complexity: O(n) for iterating through the list
#  space complexity: O(1) for using a constant amount of extra space