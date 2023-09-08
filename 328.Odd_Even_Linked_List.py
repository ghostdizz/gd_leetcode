from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        llist = ListNode()
        temp_llist = llist
        temp_head = head
        while temp_head:
            temp_llist.next = temp_head
            temp_llist = temp_llist.next
            try:
                temp_head = temp_head.next.next
            except:
                break
        temp_head = head.next
        while temp_head:
            temp_llist.next = temp_head
            temp_llist = temp_llist.next
            try:
                temp_head = temp_head.next.next
            except:
                break
        return llist.next