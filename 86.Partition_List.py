from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = ListNode()
        temp_node_1 = head1
        head2 = ListNode()
        temp_node_2 = head2
        temp_node = head
        while temp_node:
            if x > temp_node.val:
                temp_node_1.next = ListNode(temp_node.val)
                temp_node_1 = temp_node_1.next
            else:
                temp_node_2.next = ListNode(temp_node.val)
                temp_node_2 = temp_node_2.next
            temp_node = temp_node.next
        
        temp_node_1.next = head2.next
        return head1.next