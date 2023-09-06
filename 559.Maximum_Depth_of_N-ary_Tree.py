class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.max_depth = 0
    def find(self, node, level=0):
        if node is None:
            return
        level += 1
        if level > self.max_depth:
            self.max_depth = level
        for i in node.children:
            self.find(i, level)

    def maxDepth(self, root: 'Node') -> int:
        self.find(root)
        return self.max_depth