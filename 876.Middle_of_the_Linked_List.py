from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_length(self, node):
        if not node: return 0
        return 1 + self.get_length(node.next)
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.get_length(head)
        mid = int(length/2) + 1
        idx = 1
        temp_head = head
        while idx != mid:
            temp_head = temp_head.next
            idx += 1

        return temp_head