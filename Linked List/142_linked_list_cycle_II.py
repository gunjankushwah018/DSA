# Approach:
# 1. Use two pointers, slow and fast, to traverse the linked list. 
# The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. 
# If there is a cycle in the linked list, the fast pointer will eventually meet the slow pointer.
# Then find the starting point of the cycle by resetting one pointer to the head and moving both pointers one step at a time until they meet again.
# Time Complexity: O(N), where N is the number of nodes in the linked list, as we traverse the list multiple times but each traversal is linear.
# Space Complexity: O(1), as we are using only two pointers and not using any additional data structures that scale with input size.

class Solution(object):
    def detectCycle(self, head):
        fast = head
        slow = head

        # Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return None

         # Starting point of cycle
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow
