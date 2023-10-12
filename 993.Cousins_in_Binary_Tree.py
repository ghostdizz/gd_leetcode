from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.x_parents = None
        self.y_parents = None
        self.x_ = None
        self.y_ = None
    def find(self, node, level, x, y, parents = None):
        if not node: return 0
        if node.val == x:
            self.x_ = level
            self.x_parents = parents
        if node.val == y:
            self.y_ = level
            self.y_parents = parents
        if self.x_ != None and self.y_ != None:
            return 0
        self.find(node.left, level+1, x, y, node.val)
        self.find(node.right, level+1, x, y, node.val)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.find(root, 0, x, y)
        return self.x_ == self.y_ and self.x_parents != self.y_parents