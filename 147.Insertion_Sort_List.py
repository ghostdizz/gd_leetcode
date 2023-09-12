from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = head
        lst = []
        while temp_node:
            lst.append(temp_node.val)
            temp_node = temp_node.next
        head_ans = ListNode()
        curr_node = head_ans
        lst.sort()
        for i in lst:
            curr_node.next = ListNode(i)
            curr_node = curr_node.next
        head = head_ans.next
        return head