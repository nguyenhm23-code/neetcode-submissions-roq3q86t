# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode(0)
        res = cur
        remind = 0
        while l1 and l2:
            value = (l1.val + l2.val + remind) % 10
            remind = (l1.val + l2.val + remind) // 10 
            l1 = l1.next
            l2 = l2.next
            cur.next = ListNode(value)
            cur = cur.next
        while l1:
            value = (l1.val + remind) % 10
            remind = (l1.val + remind) // 10
            cur.next = ListNode(value)
            l1 = l1.next
            cur = cur.next
        while l2:
            value = (l2.val + remind) % 10
            remind = (l2.val + remind) // 10
            cur.next = ListNode(value)
            l2 = l2.next
            cur = cur.next
        if remind != 0:
            cur.next = ListNode(remind)

        return res.next