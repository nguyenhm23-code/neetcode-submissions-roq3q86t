"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new = {}
        cur = head 
        if head is None:
            return None
        while cur:
            new[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                new[cur].next = new[cur.next]
            if cur.random:
                new[cur].random = new[cur.random]
            cur = cur.next
        return new[head]
