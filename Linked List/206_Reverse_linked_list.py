# Approach 1: Traverse the linked list while reversing each node’s next pointer to point to the previous node.
# Use prev to keep track of the new head and return it after reversing the list.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev