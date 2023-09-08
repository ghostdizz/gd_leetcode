class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None        
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length: return -1
        temp_node = self.head 
        for i in range(index):
            temp_node = temp_node.next
        return temp_node.val

    def addAtHead(self, val: int) -> None:
        if not self.head and not self.tail:
            new_node = ListNode(val)
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            self.head = ListNode(val)
            self.head.next = self.tail
        else:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.head and not self.tail:
            new_node = ListNode(val)
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            self.head.next = ListNode(val)
            self.tail = self.head.next
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length: return 
        if index == 0: self.addAtHead(val)
        elif index == self.length: self.addAtTail(val)
        else:
            idx = 0
            temp_node = self.head
            while idx < index-1:
                temp_node = temp_node.next
                idx += 1
            next_node = temp_node.next
            temp_node.next = ListNode(val)
            temp_node.next.next = next_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length: return 
        if index == 0: 
            if self.length == 1:
                self.head = None
                self.tail = None
                self.length = 0
     
            else:
                temp_node = self.head
                self.head = self.head.next
                self.length -= 1
                temp_node = None
                del(temp_node)
        
        else:
            temp_node = self.head
            for i in range(index-1):
                temp_node = temp_node.next
            if index == self.length - 1:
                self.tail = temp_node
                self.tail.next = None
            else:
                next_node = temp_node.next.next
                temp_node.next = next_node
            self.length -= 1



