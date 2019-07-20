# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:

        # Two pointers:
        # Slow with one step, fast with two stpeps.
        # Slow will stop at the mid point and reverse the sub-linked list from midpoint to the end

        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Compare the reversed sub-list and the original first half

        while prev != None:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True