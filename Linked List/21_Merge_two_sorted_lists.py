# Approach:Loop through both lists and compare the values, adding the smaller one to the new list.
# Time Complexity: O(n + m) where n and m are the lengths of the two lists
# Space Complexity: O(1) since we are not using any extra space for the new list, just rearranging pointers.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next

            else:

                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1

        else:
            current.next = list2
        
        return dummy.next