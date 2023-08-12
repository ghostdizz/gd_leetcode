from typing import Optional


class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp_head = head
        temp_listnode_1 = list1
        temp_listnode_2 = list2
        while temp_listnode_1 != None and temp_listnode_2 != None:
            if temp_listnode_1.val <= temp_listnode_2.val:
                temp_head.next = temp_listnode_1
                temp_head = temp_head.next
                temp_listnode_1 = temp_listnode_1.next
            else:
                temp_head.next = temp_listnode_2
                temp_head = temp_head.next
                temp_listnode_2 = temp_listnode_2.next
        if temp_listnode_1 == None and temp_listnode_2 != None:
            temp_head.next = temp_listnode_2
            temp_head = temp_head.next
        elif temp_listnode_1 != None and temp_listnode_2 == None:
            temp_head.next = temp_listnode_1
            temp_head = temp_head.next
        return head.next


