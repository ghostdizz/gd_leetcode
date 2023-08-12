from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [item for item in lists if item is not None]
        length = len(lists)
        if length == 0:
            return None
        while length > 1:
            lists.extend(self.mergeTwoLists(lists[0], lists[1]))
            lists.pop(0)
            lists.pop(0)
            length -= 1
        return lists[0]
        
        
