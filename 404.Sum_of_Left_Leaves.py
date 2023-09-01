from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self._sum = 0

    def isLeafNode(self, node):
        if not node: return False
        return not node.left and not node.right
    
    def findLeftLeaves(self, node):
        if not node: return
        if self.isLeafNode(node.left): self._sum += node.left.val
        self.findLeftLeaves(node.left)
        self.findLeftLeaves(node.right)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.findLeftLeaves(root)
        return self._sum