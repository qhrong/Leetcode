# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = head
        prev = None
        while temp != None:
            if temp.val == val and prev != None:
                prev.next = temp.next
                temp = temp.next
            elif temp.val == val and prev == None:
                head = temp.next
                temp = head
            else:
                prev = temp
                temp = temp.next
        return head
