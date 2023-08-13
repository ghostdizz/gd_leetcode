from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head
        if head == None:
            return head
        next_node = current_node.next

        while next_node:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = next_node.next
        current_node.next = prev_node
        return current_node


