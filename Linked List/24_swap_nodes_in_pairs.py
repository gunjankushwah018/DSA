# Approach: Use a dummy node to simplify edge cases. Iterate through the linked list in pairs,
# swapping the nodes by adjusting their next pointers.
# Keep track of the previous node to connect the swapped pairs correctly.
# Time Complexity: O(L), where L is the length of the linked list.
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            left = prev.next
            right = left.next

            prev.next = right
            left.next = right.next
            right.next = left
            prev = left

        return dummy.next
