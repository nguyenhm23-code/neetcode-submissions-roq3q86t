# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        res = dummy
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                newnode = ListNode(cur1.val, None)
                res.next = newnode
                cur1 = cur1.next
            else:
                newnode = ListNode(cur2.val, None)
                res.next = newnode
                cur2 = cur2.next
            res = res.next
        while cur1:
            newnode = ListNode(cur1.val, None)
            res.next = newnode
            cur1 = cur1.next
            res = res.next
        while cur2:
            newnode = ListNode(cur2.val, None)
            res.next = newnode
            cur2 = cur2.next
            res = res.next
        return dummy.next