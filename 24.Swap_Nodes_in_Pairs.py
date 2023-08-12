from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        head1 = ListNode()
        pre_node = head1
        head1.next = head
        temp_head = head
        if head is None:
            return head
        if head.next is None:
            return head
        while temp_head != None and temp_head.next != None:
            current_node = temp_head.next.next
            temp_head_2 = temp_head.next
            pre_node.next = temp_head_2
            temp_head_2.next = temp_head
            temp_head.next = current_node
            pre_node = temp_head
            temp_head = temp_head.next
        return head1.next

