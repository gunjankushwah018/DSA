# Approach: Use two pointers, slow and fast.
# Move fast by n steps first, then move both slow and fast by one step until fast reaches the end of the list. 
# The slow pointer will be at the node just before the nth node from the end.
# Remove the nth node by changing the next pointer of the slow node.
# Time Complexity: O(L), where L is the length of the linked list.
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
        