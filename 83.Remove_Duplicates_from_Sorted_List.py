from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        temp_node = head
        next_node = temp_node.next
        while next_node:
            if temp_node.val != next_node.val:
                temp_node.next = next_node
                temp_node = temp_node.next
            next_node = next_node.next
        if temp_node.next:
            if temp_node.next.val == temp_node.val:
                temp_node.next = None
        return head