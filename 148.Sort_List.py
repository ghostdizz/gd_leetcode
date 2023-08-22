from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = head
        lst = []
        while temp_head != None:
            lst.append(temp_head.val)
            temp_head = temp_head.next
        lst.sort()
        head_return = ListNode()
        temp_return = head_return
        for i in lst:
            temp_return.next = ListNode(i)
            temp_return = temp_return.next
        return head_return.next