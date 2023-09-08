class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_node = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        new_node.prev = self.current_node
        self.current_node.next = new_node
        self.current_node = new_node   

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.current_node.prev:
                return self.current_node.val
            self.current_node = self.current_node.prev
        return self.current_node.val

    def forward(self, steps: int) -> str:
        for j in range(steps):
            if not self.current_node.next:
                return self.current_node.val
            self.current_node = self.current_node.next
        return self.current_node.val        



