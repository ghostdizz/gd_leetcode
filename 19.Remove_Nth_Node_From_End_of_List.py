from typing import Optional

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_node = head
        length_of_list_node = 0
        while temp_node is not None:
            length_of_list_node += 1
            temp_node = temp_node.next
        idx2 = length_of_list_node - n
        if idx2 == 0:
            head = head.next
        else:
            temp_node_1 = head
            idx1 = 0
            while idx1 < idx2 - 1:
                idx1 += 1
                temp_node_1= temp_node_1.next
            temp_node_2 = temp_node_1.next.next
            temp_node_1.next = temp_node_2
        return head
