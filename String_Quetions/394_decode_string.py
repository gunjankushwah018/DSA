# Approach: The idea is to use a stack to keep track of the current string and the number of times it should be repeated.
# When we encounter a digit, we build the number. When we encounter an opening
#     bracket, we push the current string and 
#     the number onto the stack and reset them. 
#     When we encounter a closing bracket, we pop from the stack 
#     and build the new string accordingly.
# Return the final string after processing all characters.
# Time complexity: O(n), where n is the length of the input string, as we are iterating through the string once.
# Space complexity: O(n), as we are using a stack to store the strings and numbers, which in the worst case can take up to n space.    

class Solution(object):
    def decodeString(self, s):
        stack=[]
        curr=""
        num=0

        for ch in s:
            if ch.isdigit():
                num = num*10+int(ch)

            elif ch.isalpha():
                curr+=ch

            elif ch == '[':
                stack.append((curr,num))
                curr=""
                num=0

            elif ch == ']':
                prev, repeat=stack.pop()
                curr=prev+curr*repeat
        return curr