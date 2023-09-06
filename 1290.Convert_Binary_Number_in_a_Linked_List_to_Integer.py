class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp_head = head
        var = 0
        while temp_head:
            var = var*10 + temp_head.val
            temp_head = temp_head.next
        
        return int(str(var), 2)   