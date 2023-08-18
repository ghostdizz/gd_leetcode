from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = 0
        i = 0
        number2 = 0
        j = 0
        temp_l1 = l1
        temp_l2 = l2
        while temp_l1:
            number1 += temp_l1.val * 10**(i)
            temp_l1 = temp_l1.next
            i += 1
        while temp_l2:
            number2 += temp_l2.val * 10**(j)
            temp_l2 = temp_l2.next
            j += 1
        number3 = number1 + number2
        l3 = ListNode()
        temp_l3 = l3
        if number3 == 0:
            return l3
        while number3 != 0:
            temp_l3.next = ListNode(number3%10)
            temp_l3 = temp_l3.next
            number3 = number3 // 10
        return l3.next
            
            