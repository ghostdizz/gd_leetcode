from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_return = ListNode()
        temp_return = head_return
        temp_sum = 0
        temp_node = head
        while temp_node:
            if temp_node.val == 0:
                if temp_sum != 0:
                    temp_return.next = ListNode(temp_sum)
                    temp_return  = temp_return.next
                temp_sum = 0
            else:
                temp_sum += temp_node.val
            temp_node = temp_node.next
        
        return head_return.next