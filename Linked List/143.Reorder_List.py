# Approach:
# 1. Find the middle of the linked list using the slow and fast pointer technique.
# 2. Reverse the second half of the linked list.
# 3. Merge the two halves of the linked list by alternating nodes from each half.
# Time Complexity: O(N), where N is the number of nodes in the linked list, as we traverse the list multiple times but each traversal is linear.
# Space Complexity: O(1), as we are modifying the list in place and not using any additional data structures that scale with input size.

class Solution(object):
    def reorderList(self, head):
        slow = head
        fast = head
        
        # 1.find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev

        # 3. Merge two halves
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next

            second.next = first.next
            first.next = second

            first = temp1
            second = temp2