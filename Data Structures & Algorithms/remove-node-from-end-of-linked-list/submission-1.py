# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        lenght = 0
        
        while cur:
            lenght += 1
            cur = cur.next
        
        if lenght == 1:
            return None
        cur = head
        while cur.next:
            if count == lenght - n - 1  :
                cur.next = cur.next.next
                break
            if lenght - n - 1 < 0:
                head = head.next
                return head
            count += 1
            cur = cur.next
        cur = head
        return cur
        
