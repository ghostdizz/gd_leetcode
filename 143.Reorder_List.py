from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 1
        lst = [head.val]
        temp_head = head.next
        while temp_head is not None:
            lst.append(temp_head.val)
            temp_head = temp_head.next
            length += 1
        if length == 1:
            return 0
        temp_head = head
        
        for i in range(int(length/2)):
            if i == 0:
                temp_head.next = ListNode(lst[length-1])
                temp_head = temp_head.next
                continue
            temp_head.next = ListNode(lst[i])
            temp_head = temp_head.next
            temp_head.next = ListNode(lst[length-i-1])
            temp_head = temp_head.next
        if length%2 == 1:
            temp_head.next = ListNode(lst[(length/2).__floor__()])
            temp_head = temp_head.next
        