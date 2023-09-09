from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def __init__(self):
        self.my_dict = {}

    def traversal(self, node, idx):
        if not node: return 
        if idx in self.my_dict:
            node.next = self.my_dict[idx]
        self.my_dict[idx] = node
        self.traversal(node.right, idx+1)
        self.traversal(node.left, idx+1)
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.traversal(root, 1)
        return root