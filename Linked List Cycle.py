# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # The idea is that if there is a cycle inside the linked list, two pointers will eventually meet each other.

        # Edge case
        if head == None:
            return False

        slow = fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False