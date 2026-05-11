# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp = []
        cur = head
        cnt = 0
        while cur:
            if cur in tmp:
                return True
            tmp.append(cur)
            cur = cur.next
        return False