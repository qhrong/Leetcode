# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None # to store the previous value
        curr = head # to store the current value
        while curr != None:
            temp = curr.next #1->2->3#
            curr.next = prev #1<-2->3#
            prev = curr #move prev one node forward
            curr = temp #move curr one node forward
        return prev



