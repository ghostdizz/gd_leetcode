from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = head
        head_return = ListNode()
        temp_return = head_return
        if temp_node is None:
            return None
        prev = None
        if prev == None and temp_node.next == None:
            return head
        while temp_node:
            if prev is None:
                if temp_node.val != temp_node.next.val:
                    temp_return.next = ListNode(temp_node.val)
                    temp_return = temp_return.next
                
            elif temp_node.next is None :
                if temp_node.val != prev.val:
                    temp_return.next = ListNode(temp_node.val)
                    temp_return = temp_return.next
                else:
                    break
            elif temp_node.val != temp_node.next.val and temp_node.val != prev.val:
                temp_return.next = ListNode(temp_node.val)
                temp_return = temp_return.next
            prev = temp_node
            temp_node = temp_node.next



        return head_return.next