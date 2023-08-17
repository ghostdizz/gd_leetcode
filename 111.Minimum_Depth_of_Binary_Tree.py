from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isLeafNode(self, node: Optional[TreeNode]) -> bool:
        if node.left is None and node.right is None:
            return True
        return False
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif self.isLeafNode(root):
            return 1
        elif root.left is None:
            return 1 + self.minDepth(root.right)

        elif root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    