from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head2 = ListNode()
        temp_head2 = head2
        head_return = ListNode()
        temp_head_return = head_return
        temp_head = head
        count = 0
        while temp_head:
            if count < k:
                count += 1
                temp_head2.next = ListNode(temp_head.val)
                temp_head2 = temp_head2.next
                temp_head = temp_head.next
            else:
                count = 0
                temp_node = self.reverse_linked_list(head2.next)
                temp_head_return.next = temp_node
                while temp_head_return.next:
                    temp_head_return = temp_head_return.next
                head2 = ListNode()
                temp_head2 = head2
        if count == k:
            temp_head_return.next = self.reverse_linked_list(head2.next)
        elif head2.next is not None:
            temp_head_return.next = head2.next
        return head_return.next


    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
    
