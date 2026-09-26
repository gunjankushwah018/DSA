# Approach : Use two pointers, slow and fast. Move slow by one step and fast by two steps.
# When fast reaches the end of the list, slow will be at the middle node.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow