from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        temp_node = head
        while temp_node:
            lst.append(temp_node.val)
            temp_node = temp_node.next
        lst2 = lst[:(left-1)] + lst[(left-1):right][::-1] + lst[right:]
        ans_node = ListNode()
        temp_node = ans_node
        for i in lst2:
            temp_node.next = ListNode(i)
            temp_node = temp_node.next
        return ans_node.next