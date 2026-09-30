# Approach: Use a dummy node to simplify edge cases.
# Iterate through both linked lists, adding corresponding digits along 
# with any carry from the previous addition. 
# Create new nodes for the resulting sum and handle 
# any remaining carry after processing both lists.
# Time Complexity: O(max(N, M)), where N and M are the lengths of the two linked lists.
# Space Complexity: O(max(N, M)), for the new linked list created to store the result.

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next