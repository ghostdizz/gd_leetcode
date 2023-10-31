from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        length = 1 
        temp_node = head
        while temp_node.next:
            temp_node = temp_node.next
            length += 1
        if k%length == 0:
            return head
        temp_node.next = head
        pre_node= temp_node
        k = k%length
        for i in range(length - k):
            head = head.next
            pre_node = pre_node.next
        pre_node.next = None
        return head
