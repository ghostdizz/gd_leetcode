from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp_head = head
        
        while temp_head != None and temp_head.val == val:
            head = head.next
            temp_head = head
        if temp_head == None:
            return head
        next_node = temp_head.next
        while next_node != None:
            while next_node != None and next_node.val == val:
                next_node = next_node.next
            temp_head.next = next_node
            temp_head = temp_head.next
            if next_node != None:
                next_node = next_node.next
        return head