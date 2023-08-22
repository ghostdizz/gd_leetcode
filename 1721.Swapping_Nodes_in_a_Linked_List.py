from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        temp_head = head
        length = 0
        while temp_head is not None:
            lst.append(temp_head.val)
            length += 1
            temp_head = temp_head.next
        
        head_return = ListNode()
        temp_return  = head_return
        for i in range(length):
            if i == k-1:
                lst[i], lst[-1-i] = lst[-1-i], lst[i]
        for j in lst:
            temp_return.next = ListNode(j)
            temp_return = temp_return.next
        return head_return.next