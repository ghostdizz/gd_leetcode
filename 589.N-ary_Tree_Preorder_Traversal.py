from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.lst = []
    def traver(self, node):
        if node is None:
            return 
        self.lst.append(node.val)
        for i in node.children:
            self.traver(i)
    def preorder(self, root: 'Node') -> List[int]:
        self.traver(root)
        return self.lst
    